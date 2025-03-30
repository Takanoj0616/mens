from django.urls import path
from. import views

urlpatterns = [
    path('', views.google_maps, name='google_maps' ),
]
