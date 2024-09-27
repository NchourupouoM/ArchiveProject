from django.db import models

# Create your models here.
class DossierJour(models.Model):
    date = models.DateField(unique=True)  # Assure qu'il n'y a qu'un dossier par jour

    def __str__(self):
        return str(self.date)

class Cellule(models.Model):
    nom = models.CharField(max_length=100)
    dossier_jour = models.ForeignKey(DossierJour, on_delete=models.CASCADE)  # Si on supprime un DossierJour, les Cellules associées sont supprimées

    def __str__(self):
        return self.nom

class Archive(models.Model):
    titre = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    fichier = models.FileField(upload_to='media/')  # Spécifier le chemin où stocker les fichiers
    metadonnees = models.JSONField(default=dict, blank=True)    
    cellule = models.ForeignKey(Cellule, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
    

