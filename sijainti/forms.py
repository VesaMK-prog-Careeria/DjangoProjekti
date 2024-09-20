from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Kalusto
from .models import Tyomaa

class RekisterointiLomake(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class KalustoForm(forms.ModelForm):
    class Meta:
        model = Kalusto
        fields = ['laite', 'sarja_nro', 'kuva', 'tila', 'kayttaja', 'tyomaa']

class TyomaaForm(forms.ModelForm):
    class Meta:
        model = Tyomaa
        fields = ['tyomaa_nro', 'alku_pvm', 'loppu_pvm']