from django.urls import path

from reader_app.views import ChannelListView, ChannelDetailView

urlpatterns = [
    path('', ChannelListView.as_view(), name='channel_list'),
    path('category/<slug:category_slug>/', ChannelListView.as_view(), name='channel_list_by_category'),
    path('<slug:slug>/', ChannelDetailView.as_view(), name='channel_detail'),
]