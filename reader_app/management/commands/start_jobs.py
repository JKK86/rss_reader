import logging

from django.core.management import BaseCommand
from django.conf import settings

import feedparser
from dateutil import parser

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from reader_app.models import Content, Channel, Category

logger = logging.getLogger(__name__)


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


def get_channels():
    return Channel.objects.all()


def delete_old_job_executions(max_age=604_800):
    """Deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = 'Runs apscheduler'

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        channels = get_channels()

        for channel in channels:
            scheduler.add_job(
                fetch_content,
                trigger="interval",
                args=(channel, ),
                minutes=2,
                id=channel.name,
                max_instances=1,
                replace_existing=True,
            )
            logger.info(f"Added job: {channel.name}")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(day_of_week="mon", hour="00", minute="00"),
            id="Delete old job executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: Delete old job executions")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
