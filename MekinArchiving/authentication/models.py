from django.contrib.auth.models import AbstractUser,Group
from django.db import models
from PIL import Image

class User(AbstractUser):
    
    USER = 'USER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = (
        (USER, 'user'),
        (ADMIN, 'admin'),
    )
    profile_photo = models.ImageField(verbose_name='Photo de profil',default='profil.png')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

    IMAGE_MAX_SIZE = (800,800)

    def resize_image(self):
        image = Image.open(self.profile_photo)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        # ce n’est pas la méthode save() du modèle !
        image.save(self.profile_photo.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
        if self.role == self.USER:
            group = Group.objects.get(name='user')
            group.user_set.add(self)
        elif self.role == self.ADMIN:
            group = Group.objects.get(name='admin')
            group.user_set.add(self)