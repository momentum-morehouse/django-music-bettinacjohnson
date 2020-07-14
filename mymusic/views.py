from django.shortcuts import render
#from the breakout rooms
from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import Album


# Create your views here.

def list_albums(request):
  mymusic = Album.objects.all()
  return render(request, "albums/list_albums.html",                        {"mymusic": mymusic})

# def index(request):
  # albums = Album.object.all()
  # return render(request, 'mymusic/list_albums.html', context={'mymusic': albums})

# def add_album(request):
#   if request.method == 'GET':
      



