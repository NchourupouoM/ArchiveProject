from django.contrib import admin

# Register your models here.

from archives.models import DossierJour, Cellule, Archive

class DossierJourAdmin(admin.ModelAdmin):
    list_display = ('date')

class CelluleAdmin(admin.ModelAdmin):
    list_display = ('nom','dossier_jour')

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('titre','date_creation','date_modification','description','fichier','metadonnees','cellule')

admin.site.register(DossierJour, DossierJourAdmin )
admin.site.register(Cellule, CelluleAdmin)
admin.site.register(Archive, ArchiveAdmin)


