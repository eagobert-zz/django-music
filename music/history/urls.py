from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.detail, name='detail'),
    path('', views.artist, name='artist'),
]