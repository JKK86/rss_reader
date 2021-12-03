from django.urls import path

from reader_app.views import ChannelListView, ChannelDetailView, FollowChannelView, UserContentListView, \
    RemoveChannelFollowingView

urlpatterns = [
    path('', ChannelListView.as_view(), name='channel_list'),
    path('category/<slug:category_slug>/', ChannelListView.as_view(), name='channel_list_by_category'),
    path('channel/<slug:slug>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('follow_channel/', FollowChannelView.as_view(), name='follow_channel'),
    path('remove_channel/<int:channel_id>/', RemoveChannelFollowingView.as_view(), name='remove_channel'),
    path('content/', UserContentListView.as_view(), name='user_content_list'),
]
