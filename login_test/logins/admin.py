from django.contrib import admin
from logins import models

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Post)
admin.site.register(models.LoginRecords)
