import feedparser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from rss_reader import settings


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)


class Channel(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    link = models.URLField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='channels')
    copyright = models.CharField(max_length=128, null=True)
    last_build_date = models.DateTimeField(null=True)
    image = models.URLField()
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="channels", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-last_build_date']

    def clean(self):
        feed = feedparser.parse(self.link)
        if feed.bozo:
            raise ValidationError("Cannot fetch the content from provided link")

    def save(self, *args, **kwargs):
        feed = feedparser.parse(self.link)
        self.name = feed.channel.get('title')
        self.slug = slugify(self.name)
        self.description = feed.channel.get('description')
        self.copyright = feed.channel.get('copyright')
        self.last_build_date = feed.channel.get('lastBuildDate')
        self.image = feed.channel.image["href"]
        if not self.category:
            category_name = feed.channel.get('category')
            if category_name:
                category, created = Category.objects.get_or_create(name=category_name)
                self.category = category
        super().save(*args, **kwargs)


class Content(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    publication_date = models.DateTimeField()
    link = models.URLField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="contents")
    guid = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.channel.name}: {self.title}'

    class Meta:
        ordering = ['-publication_date']
