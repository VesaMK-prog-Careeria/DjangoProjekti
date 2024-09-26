from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Kalusto
from .models import Tyomaa
from .models import Tyontekija
from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
class CombinedForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = Tyontekija
        fields = ['username', 'nimi', 'password1', 'password2', 'is_staff', 'is_active']

    def __init__(self, *args, **kwargs): # Tämän tarkoitus on lisätä kentät UserCreationFormiin
        super(CombinedForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(max_length=150, required=True)
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput, required=True)
        self.fields['password2'] = forms.CharField(widget=forms.PasswordInput, required=True)
        self.fields['nimi'] = forms.CharField(max_length=100, required=True)
        # radiobuttons for is_staff and is_active
        self.fields['is_staff'] = forms.BooleanField(required=False)
        self.fields['is_active'] = forms.BooleanField(required=False)

class KalustoForm(forms.ModelForm):
    class Meta:
        model = Kalusto
        fields = ['laite', 'sarja_nro', 'kuva', 'tila', 'kayttaja', 'tyomaa']

class TyomaaForm(forms.ModelForm):
    class Meta:
        model = Tyomaa
        fields = ['tyomaa_nro', 'alku_pvm', 'loppu_pvm']
        widgets = {
            'alku_pvm': forms.DateInput(attrs={'type': 'date'}),
            'loppu_pvm': forms.DateInput(attrs={'type': 'date'}),
        }