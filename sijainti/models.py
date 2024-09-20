from django.db import models
from django.contrib.auth.models import User

class Tyontekija(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nimi = models.CharField(max_length=100)

    def __str__(self):
        return self.nimi

class Tyomaa(models.Model):
    tyomaa_nro = models.CharField(max_length=10)
    alku_pvm = models.DateField()
    loppu_pvm = models.DateField()

    def __str__(self):
        return f"Työmaa {self.tyomaa_nro}"

class Kalusto(models.Model):
    TILA_VAIHTOEHDOT = [
        ('EHJÄ', 'Ehjä'),
        ('RIKKI', 'Rikki'),
        ('KÄYTÖSSÄ', 'Käytössä'),
        ('VAPAA', 'Vapaa'),
        ('HUOLLOSSA', 'Huollossa'),
    ]
    laite = models.CharField(max_length=100)
    sarja_nro = models.CharField(max_length=100)
    kuva = models.ImageField(upload_to='kuvat/', null=True, blank=True)
    tila = models.CharField(max_length=10, choices=TILA_VAIHTOEHDOT)
    kayttaja = models.ForeignKey(Tyontekija, on_delete=models.SET_NULL, null=True, blank=True)
    tyomaa = models.ForeignKey(Tyomaa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.laite

