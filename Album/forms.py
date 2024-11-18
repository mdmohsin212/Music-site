from django import forms
from Album.models import AlbumModel

class ALbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'