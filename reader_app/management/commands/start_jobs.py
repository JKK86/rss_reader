import feedparser
from dateutil import parser
from django.core.management import BaseCommand

from reader_app.models import Content, Channel, Category


def save_new_content(channel, feed):
    for item in feed.entries:
        if not Content.objects.filter(guid=item.guid).exists():
            Content.objects.create(
                title=item.title,
                description=item.description,
                publication_date=parser.parse(item.published),
                link=item.link,
                channel=channel,
                guid=item.guid
            )


def fetch_content(channel):
    feed = feedparser.parse(channel.link)
    save_new_content(channel, feed)


def get_content():
    channels = Channel.objects.all()
    for channel in channels:
        fetch_content(channel)


class Command(BaseCommand):
    help = 'Get new feeds'

    def handle(self, *args, **options):
        get_content()
