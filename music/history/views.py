from django.http import HttpResponse
from django.template import loader
from .models import Artist


# Create your views here.
def artists(request):
    artist_list = Artist.objects.order_by('-artist_name')
    template = loader.get_template('history/artists.html')
    context = {
         'artist_list': artist_list,
     }
    return HttpResponse(template.render(context, request))

def detail(request, artist_id):
    return HttpResponse("Hello, world.  You're at the artist detail page!")