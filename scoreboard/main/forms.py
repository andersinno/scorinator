from django import forms
from django.forms import Textarea
from .models import Player

class AddPlayer(forms.ModelForm):
    class Meta:
        model = Player
        fields = (
            'name',
            'score',
        )