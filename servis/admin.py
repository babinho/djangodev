from django.contrib import admin
from .models import Nalog

# Register your models here.

class NalogAdmin(admin.ModelAdmin):
    list_display = ['serviser']

admin.site.register(Nalog, NalogAdmin)
