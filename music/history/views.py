from django.http import HttpResponse
from .models import Artist


# Create your views here.
def artists(request):
    artist_list = Artist.objects.order_by('-artist_name')
    output = ', '.join([a.artist_name for a in artist_list])
    return HttpResponse(output)

def detail(request, artist_id):
    return HttpResponse("Hello, world.  You're at the artist detail page!")