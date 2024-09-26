from django.core.management.base import BaseCommand
from sijainti.models import Tyontekija

class Command(BaseCommand):
    help = 'Populate the password2 field for existing Tyontekija records'

    def handle(self, *args, **kwargs):
        for tyontekija in Tyontekija.objects.all():
            if not tyontekija.password2:
                tyontekija.password2 = 'default_password'  # Set a default value or generate a password
                tyontekija.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated password2 field for all Tyontekija records'))

# Ajetaan komento: python manage.py populate_password2
# Komento luo kaikille Tyontekija-olioille salasanan, jos sellaista ei ole