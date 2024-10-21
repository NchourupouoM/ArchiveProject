from django import forms
from . import models
from django.shortcuts import get_object_or_404

# formulaire de l'upload d'un archive 
class ArchiveForm(forms.ModelForm):
    class Meta:
        model = models.Archive
        fields = ['titre','description','fichier']

class DossierForm(forms.ModelForm):
    class Meta:
        model = models.DossierJour
        fields = ['date']

class CelluleForm(forms.ModelForm):
    class Meta:
        model = models.Cellule
        fields = ['nom','dossier_jour']

    # permet le preremplissage du champ : "dossier_jour" lors de l'enregistrement du formulaire 
    def __init__(self, *args, **kwargs):
        dossier_id = kwargs.pop('dossier_id', None)
        super().__init__(*args, **kwargs)
        if dossier_id:
            self.fields['dossier_jour'].initial = get_object_or_404(models.DossierJour, id=dossier_id)
            self.fields['dossier_jour'].widget = forms.HiddenInput()  # Pour masquer le champ   