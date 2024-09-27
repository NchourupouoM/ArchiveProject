from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import archives
import archives.views

urlpatterns = [
    path('home/',archives.views.home,name='home'),
]