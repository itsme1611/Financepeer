from django.contrib import admin
from django.contrib.auth.models import User
from api_v1 import models

# Register your models here.
# admin.site.register(User)
admin.site.register(models.FileDocument)