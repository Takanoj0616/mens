from django.urls import path
from list.views import therapist_profile
from. import views


urlpatterns = [
    #セラピスト詳細
    path('profile/<uuid:id>', views.therapist_profile, name='therapist-profile'),
    #セラピスト一覧
    path('', views.therapist_list, name='therapist-list'),
    path('now', views.realtime_now, name='realtime-now'),
    path('realtime', views.realtime_now, name='realtime-now'),
]
