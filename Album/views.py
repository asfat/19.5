from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import Album
from . import forms
from django.urls import reverse_lazy
from . import models
# Create your views here.
def album(request):
    return render(request,'album.html')

class AlbumCreate(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name=	'album.html'
    success_url = 'home'	
    def get_success_url(self):
        return reverse_lazy('home')
    
def home(request):
    album=Album.objects.all()
    return render(request,'home.html',{'album':album})

def editAlbum(request,id):
    album=models.Album.objects.get(pk=id)
    albumForm=forms.AlbumForm(instance=album)
    if request.method == 'POST':
        albumForm=forms.AlbumForm(request.POST,instance=album)
        if albumForm.is_valid():
            albumForm.save()
            return redirect('home')
    return render(request,'editalbum.html',{'form':albumForm})

def deletealbum(request,id):
    album=models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')