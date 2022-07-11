from unicodedata import name
from django.contrib import admin
from . import models

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(models.Student, StudentAdmin)
