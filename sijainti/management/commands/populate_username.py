from django.core.management.base import BaseCommand
from sijainti.models import Tyontekija

class Command(BaseCommand):
    help = 'Populate the password2 field for existing Tyontekija records'

    def handle(self, *args, **kwargs):
        for tyontekija in Tyontekija.objects.all():
            if not tyontekija.username:
                tyontekija.username = f'user_{tyontekija.id}'  # Set a default value or generate a username
                tyontekija.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated password2 field for all Tyontekija records'))

# Ajetaan komento: python manage.py populate_username
# Komento luo kaikille Tyontekija-olioille käyttäjänimen, jos sellaista ei ole