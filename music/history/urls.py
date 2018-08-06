from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    path('artist/<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album_detail'),
    #path('albums/new', views.album_new, name='album_new')
]