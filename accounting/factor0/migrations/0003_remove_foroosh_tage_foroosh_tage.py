# Generated by Django 5.0 on 2024-01-08 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factor0', '0002_alter_foroosh_shomare_factor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foroosh',
            name='tage',
        ),
        migrations.AddField(
            model_name='foroosh',
            name='tage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='factor0.tage'),
        ),
    ]
