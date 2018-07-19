from django.http import HttpResponse

# Create your views here.
    
def artists(request):
    return HttpResponse("Hello, world.  You're at the artist page!")

def detail(request, artist_id):
    return HttpResponse("Hello, world.  You're at the artist detail page!")