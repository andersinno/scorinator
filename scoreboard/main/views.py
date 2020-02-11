from django.shortcuts import render, redirect
from django.contrib import messages
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
        if not int(request.POST['score']) > 9223372036854775807:
            Player(name=request.POST['name'], score=request.POST['score']).save()
        else:
            messages.warning(request, f'The score is to high')

    return redirect('home')
