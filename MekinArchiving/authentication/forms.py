from django import forms
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,label="Nom d'utilisateur")
    password = forms.CharField(max_length=63,widget=forms.PasswordInput,label="Mot de passe")


class PhotoProfil(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['profile_photo']