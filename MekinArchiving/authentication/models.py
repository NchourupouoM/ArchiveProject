from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    USER = 'USER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = (
        (USER, 'user'),
        (ADMIN, 'admin'),
    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')