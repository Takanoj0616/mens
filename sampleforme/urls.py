from django.urls import path
from .views import PostCreateView, PostConfirmView, PostCompleteView, PostListView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('confirm/', PostConfirmView.as_view(), name='post_confirm'),
    path('complete/', PostCompleteView.as_view(), name='post_complete'),
    path('', PostListView.as_view(), name='post_list'),
]
