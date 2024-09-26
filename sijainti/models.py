from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager

class TyontekijaManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)
class Tyontekija(AbstractBaseUser, PermissionsMixin): #AbstractBaseUser ja PermissionsMixin luokat periytyvät
    username = models.CharField(max_length=150, unique=True)
    password1 = models.CharField(max_length=150)
    nimi = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='tyontekija_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    objects = TyontekijaManager()

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='tyontekija_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nimi']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.password1 == self.password2:
            raise ValueError('Passwords do not match')
        self.set_password(self.password1)
        super().save(*args, **kwargs)

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

# python manage.py makemigrations
# python manage.py migrate