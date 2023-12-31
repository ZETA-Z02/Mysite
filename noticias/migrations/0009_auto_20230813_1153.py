# Generated by Django 3.1.3 on 2023-08-13 16:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0008_auto_20230802_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.CharField(default=None, max_length=200, validators=[django.core.validators.RegexValidator(message='Correo invalido', regex='\\S{20}@\\S{10}\\.\\S{3}')], verbose_name='Correo Electronico'),
        ),
    ]
