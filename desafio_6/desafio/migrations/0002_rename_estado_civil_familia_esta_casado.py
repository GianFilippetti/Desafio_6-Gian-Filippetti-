# Generated by Django 3.2.16 on 2022-12-25 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familia',
            old_name='estado_civil',
            new_name='esta_casado',
        ),
    ]
