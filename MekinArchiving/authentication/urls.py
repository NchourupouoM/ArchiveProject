from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
import authentication
import authentication.views

urlpatterns = [
    path('',LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user =True),
        name="login"),
    path('logout/',authentication.views.logout_user, name='logout'),
]