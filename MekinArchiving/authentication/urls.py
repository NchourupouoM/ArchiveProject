from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView,PasswordChangeView

import authentication.views

urlpatterns = [
    path('',authentication.views.LoginPageView.as_view(), name = 'login'),
    path('mon-compte/',authentication.views.mon_compte,name='mon-compte'),
    path('logout/',authentication.views.logout_user, name='logout'),
    path('change-password/',PasswordChangeView.as_view(
        template_name = "authentication/change_password_form.html",
    ),name='password_change'),
    path('change-password-done/',PasswordChangeDoneView.as_view(
        template_name = "authentication/change_password_done.html",
    ),name="password_change_done"),
    path('change-profil/',authentication.views.photo_upload,name='change-profil'),
    path('addUser/',authentication.views.signup_page,name='signup'),
]