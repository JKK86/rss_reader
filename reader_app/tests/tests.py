import pytest

from reader_app.models import Channel, Category, Content


@pytest.mark.django_db
def test_category_create(set_up):
    assert Category.objects.count() == len(set_up[0])
    assert Category.objects.first().name == "Test category 0"


@pytest.mark.django_db
def test_channel_create(set_up):
    assert Channel.objects.count() == len(set_up[1])
    channel0 = Channel.objects.last()
    assert channel0.name == "Channel 0"
    assert channel0.link == "https://channel0.com"


@pytest.mark.django_db
def test_content_create(set_up):
    assert Content.objects.count() == len(set_up[2])
    content0 = Content.objects.last()
    assert content0.title == "Episode 0"
    assert content0.description == "This is episode 0"
