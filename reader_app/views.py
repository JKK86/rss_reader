from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateResponseMixin

from reader_app.models import Content, Channel, Category


class ChannelListView(TemplateResponseMixin, View):
    model = Channel
    template_name = "rss_reader/channel_list.html"

    def get(self, request, category_slug=None):
        channel_list = Channel.objects.all()
        categories = Category.objects.annotate(total_channels=Count('channels'))
        category = None
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            channel_list = channel_list.filter(category=category)
        paginator = Paginator(channel_list, 10)
        page = request.GET.get('page', 1)
        try:
            channels = paginator.page(page)
        except PageNotAnInteger:
            channels = paginator.page(1)
        except EmptyPage:
            channels = paginator.page(paginator.num_pages)

        return self.render_to_response({'categories': categories,
                                        'category': category,
                                        'channels': channels})


class ChannelDetailView(DetailView):
    model = Channel
    template_name = "rss_reader/channel_detail.html"
