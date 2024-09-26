from django.test import TestCase
from .models import Kalusto, Tyontekija, Tyomaa

class KalustoTestCase(TestCase):
    def setUp(self): # Luodaan testitietokanta
        Tyontekija.objects.create(username="testi", password1="salasana", nimi="Testi Testinen")
        Kalusto.objects.create(laite="Porakone", tila="VAPAA")
        
    def test_kalusto_luonti(self): # Testataan, että kalusto on luotu oikein
        porakone = Kalusto.objects.get(laite="Porakone")
        self.assertEqual(porakone.tila, "VAPAA")

    def test_kalusto_muokkaus(self): # Testataan, että kaluston tilaa voidaan muokata
        porakone = Kalusto.objects.get(laite="Porakone")
        porakone.tila = "KÄYTÖSSÄ"
        porakone.save()
        self.assertEqual(porakone.tila, "KÄYTÖSSÄ")

class TyomaaTestCase(TestCase):
    def setUp(self): # Luodaan testitietokanta
        Tyomaa.objects.create(tyomaa_nro="123", alku_pvm="2023-01-01", loppu_pvm="2023-12-31")

    def test_tyomaa_luonti(self): # Testataan, että työmaa on luotu oikein
        tyomaa = Tyomaa.objects.get(tyomaa_nro="123")
        self.assertEqual(tyomaa.alku_pvm.strftime("%Y-%m-%d"), "2023-01-01")
        #strftime metodi muuttaa päivämäärän merkkijonoksi joka on vertailtavissa

    def test_tyomaa_muokkaus(self): # Testataan, että työmaan alkupäivämäärää voidaan muokata
        tyomaa = Tyomaa.objects.get(tyomaa_nro="123")
        tyomaa.alku_pvm = "2023-02-01"
        tyomaa.save()
        self.assertEqual(tyomaa.alku_pvm, "2023-02-01")

#python manage.py test sijainti
