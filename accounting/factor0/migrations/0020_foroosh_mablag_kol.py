# Generated by Django 4.2.8 on 2024-01-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factor0', '0019_remove_foroosh_jame_kol'),
    ]

    operations = [
        migrations.AddField(
            model_name='foroosh',
            name='Mablag_kol',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
