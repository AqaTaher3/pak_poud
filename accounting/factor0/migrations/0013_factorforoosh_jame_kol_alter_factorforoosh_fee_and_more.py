# Generated by Django 4.2.8 on 2023-12-31 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factor0', '0012_alter_tage_metraj'),
    ]

    operations = [
        migrations.AddField(
            model_name='factorforoosh',
            name='Jame_kol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='factorforoosh',
            name='fee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tage',
            name='vazn',
            field=models.IntegerField(),
        ),
    ]
