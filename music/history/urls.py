from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('history/artists/details', views.details, name='details'),
    path('history/artists', views.artists, name='artists'),
]