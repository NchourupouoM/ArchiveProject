from django import forms
from . import models

# formulaire de l'upload d'un archive 
class ArchiveForm(forms.ModelForm):
    class Meta:
        model = models.Archive
        fields = ['titre','description','fichier','metadonnees']