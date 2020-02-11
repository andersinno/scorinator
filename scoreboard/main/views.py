from django.shortcuts import render
from .forms import AddPlayer

# Create your views here.


def home(request):
    return render(request, "main/main.html")


def addEntry(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, "main/main.html")
