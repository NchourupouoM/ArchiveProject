from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    message = "Bienvenu"
    return render(request,'archives/home.html', {"message": message})

def Dossier(request):
    dossiers = models.DossierJour.objects.all()
    return render(request=request, template_name="archives/dossiersjours.html",context={"dossiers":dossiers})

def cellule(request,dossier_id):
    dossier = get_object_or_404(models.DossierJour,id=dossier_id)
    cellules = dossier.cellule_set.all()
    return render(request,'archives/cellule_view.html',{'cellules':cellules})

def archives_view(request,cellule_id):
    cellule = get_object_or_404(models.Cellule,id=cellule_id)
    archives = cellule.archive_set.all()
    return render(request,'archives/archives_view.html',{'archives':archives})