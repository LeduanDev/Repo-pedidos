from django.urls import path, include
from productos import views


urlpatterns = [
    path('', views.inicio, name='inicio')    
]