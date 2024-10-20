from django.db import models
from datetime import datetime
from django.conf import settings


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, related_name='message_room', on_delete=models.CASCADE)   