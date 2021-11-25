from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    copyright = models.CharField(max_length=128)
    last_build_date = models.DateTimeField()
    image = models.URLField()

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    publication_date = models.DateTimeField()
    link = models.URLField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    guid = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.channel.name}: {self.title}'
