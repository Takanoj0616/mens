from django.urls import path
from . import views

urlpatterns = [
    path('', views.topics_view, name='topics'),
    path('plus', views.topics_view2, name='topics2'),
]
