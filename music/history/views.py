from django.shortcuts import get_object_or_404, render
from .models import Artist


# Create your views here.
def artists(request):
    artist_list = Artist.objects.order_by('-artist_name')
    context = {
         'artist_list': artist_list,
     }
    return render(request, 'history/artists.html', context)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'history/detail.html', {'artist': artist})