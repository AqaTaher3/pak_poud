# Generated by Django 5.0 on 2024-01-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factor0', '0032_alter_hesab_daryafti_nagdi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hesab_daryafti',
            name='daftari',
        ),
        migrations.AddField(
            model_name='hesab_daryafti',
            name='daftari',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
