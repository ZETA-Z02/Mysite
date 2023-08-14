# Generated by Django 3.1.3 on 2023-08-14 01:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0009_auto_20230813_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='image',
            field=models.ImageField(default=None, upload_to='images/', verbose_name='imagen a subir'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.CharField(default=None, max_length=200, validators=[django.core.validators.RegexValidator(message='Correo invalido', regex='\\S{4}@\\S{5}\\.\\S{3}')], verbose_name='Correo Electronico'),
        ),
    ]