from django.contrib import admin
from .models import Player
# Register your models here.

lista = [Player]
admin.site.register(lista)