from django.shortcuts import render, redirect
from Album.forms import ALbumForm
from Album.models import AlbumModel
# Create your views here.

def album(request):
    if request.method == 'POST':
        form = ALbumForm(request.POST)
        if form.is_valid():
            form.save()
            form = ALbumForm()
    else:
        form = ALbumForm()
    return render(request, 'album.html', {'form' : form})

def edit(request, id):
    album = AlbumModel.objects.get(pk=id)
    album_form = ALbumForm(instance=album)
    if request.method == 'POST':
        post_form = ALbumForm(request.POST, instance=album)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
        
    return render(request, 'album.html', {'form' : album_form})

