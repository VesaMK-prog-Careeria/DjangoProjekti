from django.shortcuts import render, redirect, get_object_or_404
from .models import Kalusto, Tyomaa, Tyontekija
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import KalustoForm, TyomaaForm, CombinedForm, LoginForm
from django.contrib.auth import logout, login, authenticate

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('etusivu')  # Redirect to a success page.
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@never_cache # Tämä rivi estää sivun välimuistin käytön
@login_required
def etusivu(request):
    return render(request, 'base.html')

#Työntekijä lisäys
@never_cache # Tämä rivi estää sivun välimuistin käytön
@login_required
def tyontekija_lisays(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etusivu')
    else:
        form = CombinedForm()
    return render(request, 'tyontekija_lisays.html', {'form': form})

@never_cache # Tämä rivi estää sivun välimuistin käytön
@login_required # Tämä rivi vaatii kirjautumisen
def kalusto_lista(request):
    kalustot = Kalusto.objects.all()
    return render(request, 'kalusto_lista.html', {'kalustot': kalustot})

@never_cache
@login_required
def tyomaa_lista(request):
    tyomaat = Tyomaa.objects.all()
    return render(request, 'tyomaa_lista.html', {'tyomaat': tyomaat})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def kalusto_lisays(request):
    if request.method == 'POST':
        form = KalustoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kalusto_lista')
    else:
        form = KalustoForm()
    return render(request, 'kalusto_lisays.html', {'form': form})

@login_required
def kalusto_muokkaus(request, pk):
    kalusto = Kalusto.objects.get(pk=pk)
    if request.method == 'POST':
        form = KalustoForm(request.POST, request.FILES, instance=kalusto)
        if form.is_valid():
            form.save()
            return redirect('kalusto_lista')
    else:
        form = KalustoForm(instance=kalusto)
    return render(request, 'kalusto_muokkaus.html', {'form': form})

@login_required
def kalusto_poisto(request, pk):
    kalusto = get_object_or_404(Kalusto, pk=pk)
    if request.method == 'POST':
        kalusto.delete()
        return redirect('kalusto_lista')
    return render(request, 'kalusto_poisto.html', {'kalusto': kalusto})

@login_required
def tyomaa_lisays(request):
    if request.method == 'POST':
        form = TyomaaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tyomaa_lista')
    else:
        form = TyomaaForm()
    return render(request, 'tyomaa_lisays.html', {'form': form})

@login_required
def tyomaa_muokkaus(request, pk):
    tyomaa = Tyomaa.objects.get(pk=pk)
    if request.method == 'POST':
        form = TyomaaForm(request.POST, instance=tyomaa)
        if form.is_valid():
            form.save()
            return redirect('tyomaa_lista')
    else:
        form = TyomaaForm(instance=tyomaa)
    return render(request, 'tyomaa_muokkaus.html', {'form': form})

@login_required
def tyomaa_poisto(request, pk):
    tyomaa = get_object_or_404(Tyomaa, pk=pk)
    if request.method == 'POST':
        tyomaa.delete()
        return redirect('tyomaa_lista')
    return render(request, 'tyomaa_poisto.html', {'tyomaa': tyomaa})