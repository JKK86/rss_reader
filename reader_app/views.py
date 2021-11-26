from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from reader_app.models import Content


class LandingPageView(ListView):
    template_name = "rss_reader/landing_page.html"
    model = Content

    def get_context_data(self, **kwargs):
        context = super(LandingPageView, self).get_context_data(**kwargs)
        context["contents"] = Content.objects.filter()[:10]
        return context
