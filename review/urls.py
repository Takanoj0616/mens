from django.urls import path
from .views import ReviewCreateView, ReviewConfirmView, SuccessView, ReviewListView

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('confirm/', ReviewConfirmView.as_view(), name='review_confirm'),
    path('success/', SuccessView.as_view(), name='review_success'),
    path('create/', ReviewCreateView.as_view(), name='review_create'),
]
