from django.shortcuts import render
from .forms import AddPlayer

# Create your views here.


def home(request):
    return render(request, "main/main.html")
