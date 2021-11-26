import random
import string

import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone

from reader_app.models import Category, Channel, Content

User = get_user_model()


@pytest.fixture
def create_test_user():
    return User.objects.create_user('Test_user', 'user@test.com', 'test')


@pytest.fixture
def set_up(create_test_user):
    categories = []
    channels = []
    contents = []

    for i in range(3):
        categories.append(Category.objects.create(
            name=f"Test category {i}",
            slug=f"test-category-{i}"
        ))

    for i in range(5):
        channels.append(Channel.objects.create(
            name=f"Channel {i}",
            link=f"https://channel{i}.com",
            description=f"This is channel {i}",
            category=random.choice(categories),
            copyright=f"Copyright 2021, Channel {i}",
            last_build_date=timezone.now(),
            image=f"https://image.channel{i}.com",
        ))

    for i in range(10):
        channel = random.choice(channels)
        contents.append(Content.objects.create(
            channel=channel,
            title=f"Episode {i}",
            description=f"This is episode {i}",
            publication_date=timezone.now(),
            link=f"https://{channel.name}.episode{i}.com",
            guid="".join(random.choices((string.ascii_lowercase + string.digits), k=10)),
        ))

    return [categories, channels, contents]
