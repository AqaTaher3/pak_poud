# Generated by Django 4.2.8 on 2024-01-01 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer0', '0002_zinaf_moshtary_kode_meli_alter_moshtary_name'),
        ('factor0', '0016_alter_factorforoosh_kharidar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FactorForoosh',
            new_name='Foroosh',
        ),
    ]
