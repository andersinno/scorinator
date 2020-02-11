from django.shortcuts import render, redirect
from .forms import AddPlayer
from .models import Player
# Create your views here.


def home(request):
    toHTML = {
        'players': Player.objects.all().order_by('-score'),
        'form': AddPlayer()
    }
    return render(request, "main/main.html", toHTML)


def addEntry(request):
    if request.method == 'POST':
        Player(name=request.POST['name'], score=request.POST['score']).save()
    return redirect('home')
