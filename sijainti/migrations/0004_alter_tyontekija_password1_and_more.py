# Generated by Django 5.1.1 on 2024-09-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sijainti', '0003_tyontekija_groups_tyontekija_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tyontekija',
            name='password1',
            field=models.CharField(default=12345, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tyontekija',
            name='password2',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='tyontekija',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
