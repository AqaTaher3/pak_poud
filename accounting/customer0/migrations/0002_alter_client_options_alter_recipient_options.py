# Generated by Django 5.0 on 2024-01-09 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer0', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['name'], 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='recipient',
            options={'ordering': ['-name'], 'verbose_name_plural': 'Recipients'},
        ),
    ]
