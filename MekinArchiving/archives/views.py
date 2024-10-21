from django.shortcuts import render, redirect
from archives.models import Cellule,DossierJour
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from . import forms
from authentication.models import User
from datetime import date
# Create your views here.
@login_required
def home(request):
    message = "Bienvenu"
    return render(request,'archives/home.html', {"message": message})
# ========================================================================

@login_required
def Dossier(request):
    dossiers = DossierJour.objects.all()
    return render(request=request, template_name="archives/dossiersjours.html",context={"dossiers":dossiers})
# =========================================================================

@login_required
def cellule(request,dossier_id):
    dossier = get_object_or_404(DossierJour,id=dossier_id)
    cellules = dossier.cellule_set.all()
    today = date.today()
    return render(request,'archives/cellule_view.html',{'cellules':cellules,"dossier_id":dossier.id,"today":today})
# =========================================================================

@login_required
def list_archives_view(request,cellule_id): 
    cellule = get_object_or_404(Cellule,id=cellule_id)
    archives = cellule.archive_set.all()
    dossier_id = cellule.dossier_jour.pk
    return render(request,'archives/list_archives_view.html',{'archives':archives,"dossier_id":dossier_id})
# =========================================================================

@login_required
def upload_archive(request, cellule_id):
    cellule = get_object_or_404(Cellule, id=cellule_id)
    form = forms.ArchiveForm()
    if request.method == 'POST':
        form = forms.ArchiveForm(request.POST,request.FILES)
        if form.is_valid():
            archive = form.save(commit=False)
            archive.uploader = request.user
            archive.cellule = cellule
            archive.save()
            return redirect('archive',cellule_id=cellule_id)
    cellule = cellule.dossier_jour.id
    return render(request=request,template_name='archives/upload_archive.html',context={'form':form,'cellule':cellule})
# =========================================================================

@login_required
def dashboard(request):
    
    return render(request,"archives/dashboard.html")
# =========================================================================

@login_required
@permission_required('dossier.add_dossier')
def creerDossier(request):
    form = forms.DossierForm()
    if request.method=='POST':
        form = forms.DossierForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dossier')
    return render(request,"archives/creer_dossier.html",{"form":form})
# =========================================================================

@login_required
@permission_required('cellule.add_cellule')
def creerCellule(request,dossier_id):
    form = forms.CelluleForm(request.POST or None, dossier_id=dossier_id)
    if request.method=='POST':
        form = forms.CelluleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="cellule",dossier_id=dossier_id)
    return render(request,"archives/creer_cellule.html",{"form":form,"dossier_id":dossier_id})