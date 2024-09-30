from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import archives
import archives.views

urlpatterns = [
    path('home/',archives.views.home,name='home'),
    path('dossier/',archives.views.Dossier, name='dossier'),
    path('cellules/<int:dossier_id>', archives.views.cellule, name='cellule'),
    path('documents/<int:cellule_id>', archives.views.list_archives_view, name="archive"),
    path('document/<int:cellule_id>/upload',archives.views.upload_archive, name='upload'),
]