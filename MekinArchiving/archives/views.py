from django.shortcuts import render, redirect
from . import models
from django.shortcuts import get_object_or_404
from . import forms

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

def list_archives_view(request,cellule_id):
    cellule = get_object_or_404(models.Cellule,id=cellule_id)
    archives = cellule.archive_set.all()
    return render(request,'archives/list_archives_view.html',{'archives':archives})

def upload_archive(request, cellule_id):
    cellule = get_object_or_404(models.Cellule, id=cellule_id)
    form = forms.ArchiveForm()
    if request.method == 'POST':
        form = forms.ArchiveForm(request.POST,request.FILES)
        if form.is_valid():
            archive = form.save(commit=False)
            archive.uploader = request.user
            archive.cellule = cellule
            archive.save()
            return redirect('dossier')
    return render(request=request,template_name='archives/upload_archive.html',context={'form':form,'cellule':cellule})