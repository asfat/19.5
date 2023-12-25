from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Musician

class MusicianCreationForm(UserCreationForm):
    instrument_type = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('instrument_type', )

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['instrument_type']