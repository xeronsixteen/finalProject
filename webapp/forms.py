from django import forms
from django.forms import widgets

from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description', 'album', 'public']
        # widgets = {
        #     'album': widgets.RadioSelect
        # }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['user']
        widgets = {
            'created_at': widgets.SelectDateWidget,
        }


class AlbumFormUser(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['user']


class UserForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['user']
        widgets = {'user': widgets.CheckboxSelectMultiple}
