from django import forms
from .models import Album

class albumsForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'album_title',
            'artist_Name',
            'released',    
        ]
