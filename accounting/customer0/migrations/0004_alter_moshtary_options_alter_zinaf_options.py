# Generated by Django 5.0 on 2024-01-07 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer0', '0003_alter_moshtary_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moshtary',
            options={'ordering': ['name'], 'verbose_name_plural': 'Moshtari_ha'},
        ),
        migrations.AlterModelOptions(
            name='zinaf',
            options={'ordering': ['-name'], 'verbose_name_plural': 'Zinaf_ha'},
        ),
    ]
