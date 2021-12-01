from django.urls import path

from reader_app.views import ChannelListView, ChannelDetailView, UserFollowChannelView, UserContentListView

urlpatterns = [
    path('', ChannelListView.as_view(), name='channel_list'),
    path('category/<slug:category_slug>/', ChannelListView.as_view(), name='channel_list_by_category'),
    path('channel/<slug:slug>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('follow_channel/', UserFollowChannelView.as_view(), name='follow_channel'),
    path('content/', UserContentListView.as_view(), name='user_content_list'),
]
