from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.
class DossierJour(models.Model):
    date = models.DateField(unique=True,default=date.today())  # Assure qu'il n'y a qu'un dossier par jour
    count_in_other_table = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.date)
    def get_instance(self):
        count= Cellule.objects.filter(dossier_jour=self.pk)
        self.count_in_other_table = count.count()


    def save(self,*args,**kwargs):
        if self.pk:
            self.get_instance()
        super().save(*args,**kwargs)


class Cellule(models.Model):
    nom = models.CharField(max_length=100)
    dossier_jour = models.ForeignKey(DossierJour, on_delete=models.CASCADE)  # Si on supprime un DossierJour, les Cellules associées sont supprimées

    def __str__(self):
        return self.nom
    

class ArchiveManager(models.Manager):
    def published(self):
        return self.filter(status='published')

class Archive(models.Model):
    titre = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    fichier = models.FileField(upload_to='')  # Spécifier le chemin où stocker les fichiers
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    cellule = models.ForeignKey(Cellule, on_delete=models.CASCADE)
    published = ArchiveManager()

    def __str__(self):
        return self.titre
    

