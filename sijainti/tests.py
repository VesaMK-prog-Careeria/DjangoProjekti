from django.test import TestCase
from .models import Kalusto, Tyontekija, Tyomaa

class KalustoTestCase(TestCase):
    # def setUp(self):
    #     Tyontekija.objects.create(nimi="Testi Käyttäjä")
    #     Tyomaa.objects.create(tyomaa_nro="123", alku_pvm="2023-01-01", loppu_pvm="2023-12-31")
    #     Kalusto.objects.create(laite="Porakone", sarja_nro="ABC123", tila="VAPAA")

    # def test_kalusto_luonti(self):
    #     porakone = Kalusto.objects.get(laite="Porakone")
    #     self.assertEqual(porakone.tila, "VAPAA")

    def test_kalusto_muokkaus(self):
        porakone = Kalusto.objects.get(laite="Laattaleikkuri")
        porakone.tila = "KÄYTÖSSÄ"
        porakone.save()
        self.assertEqual(porakone.tila, "KÄYTÖSSÄ")

# class TyomaaTestCase(TestCase):
#     def setUp(self):
#         Tyomaa.objects.create(tyomaa_nro="123", alku_pvm="2023-01-01", loppu_pvm="2023-12-31")

#     def test_tyomaa_luonti(self):
#         tyomaa = Tyomaa.objects.get(tyomaa_nro="123")
#         self.assertEqual(tyomaa.alku_pvm, "2023-01-01")

#     def test_tyomaa_muokkaus(self):
#         tyomaa = Tyomaa.objects.get(tyomaa_nro="123")
#         tyomaa.alku_pvm = "2023-02-01"
#         tyomaa.save()
#         self.assertEqual(tyomaa.alku_pvm, "2023-02-01")

#python manage.py test sijainti
