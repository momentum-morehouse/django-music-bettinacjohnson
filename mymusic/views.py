from django.shortcuts import render, redirect, get_object_or_404
#from the breakout rooms
# from django.db import models
from .models import Album
from .forms import albumsForm


# Create your views here.

def list_albums(request):
  albums = Album.objects.all()
  return render(request, "albums/list_albums.html",                        {"albums": albums})

def add_album(request):
    if request.method == 'GET':
        form = albumsForm()
    else:
        form = albumsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_album.html", {"form": form})  

# def delete_albums(request, pk):
#     album = get_object_or_404(Album, pk=pk)
#     if request.method == 'POST':
#         album.delete()
#         return redirect(to='list_albums')
#     return render(request, "mymusic/delete_album.html", context={"albums": album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html",
                  {"album": album})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = albumsForm(instance=album)
    else:
        form = albumsForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })
