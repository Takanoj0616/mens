from django.urls import path
from. import views


urlpatterns = [
    path('', views.therapist_new_list, name='therapist_new_list'),
]