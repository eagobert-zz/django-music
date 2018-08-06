from django.views.generic import TemplateView, ListView, DetailView
from .models import Artist, Album
from .forms import AlbumForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'history/index.html'

    # "location" gets attached to a built-in object in the template called 'view'
    def location(self):
        return 'home'

class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artist_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "artists"
        return context

class ArtistDetailView(DetailView):
    model = Artist

class AlbumListView(ListView):
    model = Album
    context_object_name = 'album_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "albums"
        return context

class AlbumDetailView(DetailView):
    model: Album

# def album_new(request):
#     form = AlbumForm()
#     return render(request, 'history/album_new.html', {'form': form})