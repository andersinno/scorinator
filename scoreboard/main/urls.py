from django.urls import path, register_converter
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addEntry, name='add'),
]
