from django.urls import path

from reader_app.views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page')
]