from django.urls import path

import authentication.views

urlpatterns = [
    path('',authentication.views.LoginPageView.as_view(), name = 'login'),
    path('logout/',authentication.views.logout_user, name='logout'),
]