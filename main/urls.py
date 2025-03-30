from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('system/', views.SystemView.as_view(), name='system'),
    path('recruit/', views.RecruitView.as_view(), name='recruit'),
]
