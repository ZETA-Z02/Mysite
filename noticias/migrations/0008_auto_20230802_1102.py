# Generated by Django 3.1.3 on 2023-08-02 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0007_auto_20230802_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='teléfono',
            new_name='telefono',
        ),
    ]
