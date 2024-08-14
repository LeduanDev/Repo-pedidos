from django.urls import path, include
from productos import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.inicio, name='inicio')    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)