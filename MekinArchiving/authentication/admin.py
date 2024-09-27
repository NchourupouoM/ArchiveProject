from django.contrib import admin

# Register your models here.
from authentication.models import User

class UserAmin(admin.ModelAdmin):
    list_display = ('username','role')


admin.site.register(User, UserAmin)