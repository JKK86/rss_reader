from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import TemplateResponseMixin

from reader_app.forms import ChannelFollowForm
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
                                        'channels': channels,})


class ChannelDetailView(DetailView):
    model = Channel
    template_name = "rss_reader/channel_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['follow_form'] = ChannelFollowForm(initial={'channel': self.object})
        return context


class UserFollowChannelView(LoginRequiredMixin, FormView):
    channel = None
    form_class = ChannelFollowForm

    def form_valid(self, form):
        self.channel = form.cleaned_data['channel']
        self.channel.followers.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_content_list')


class UserContentListView(LoginRequiredMixin, ListView):
    model = Content
    template_name = 'rss_reader/user_content_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(channel__followers__in=[self.request.user])[:10]
