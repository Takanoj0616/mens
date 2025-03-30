
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import viewsets, routers, serializers

from map.models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'lat', 'lng')

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# ルーターの登録
router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('list/', include('list.urls')),
    path('newface/', include('newface.urls')),
    path('map/', include('map.urls')),
    path('gmap/api/', include(router.urls)),  # APIエンドポイント
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('review/', include('review.urls')),
    path('schedule/', include('schedule.urls')),
    path('topics1/', include('topics1.urls')),
    path('topics2/', include('topics1.urls')),
    path('realtime/', include('list.urls')),
    path('sampleforme', include('sampleforme.urls')), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)