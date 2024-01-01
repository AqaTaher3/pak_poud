# Generated by Django 4.2.8 on 2024-01-01 11:04

from django.db import migrations, models
import factor0.models


class Migration(migrations.Migration):

    dependencies = [
        ('customer0', '0002_zinaf_moshtary_kode_meli_alter_moshtary_name'),
        ('factor0', '0014_factorforoosh_shomare_factor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factorforoosh',
            options={'ordering': ['-shomare_factor']},
        ),
        migrations.AlterModelOptions(
            name='tage',
            options={'ordering': ['-jens_parche', '-vazn', '-metraj']},
        ),
        migrations.RemoveField(
            model_name='factorforoosh',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='factorforoosh',
            name='tage_ha',
        ),
        migrations.AddField(
            model_name='factorforoosh',
            name='tage',
            field=models.ManyToManyField(blank=True, null=True, to='factor0.tage'),
        ),
        migrations.AddField(
            model_name='tage',
            name='geymat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tage',
            name='rangrazi',
            field=models.CharField(default='sooper_derakhshan', max_length=30),
        ),
        migrations.RemoveField(
            model_name='factorforoosh',
            name='kharidar',
        ),
        migrations.AlterField(
            model_name='tage',
            name='jens_parche',
            field=models.CharField(default='nil-bangal', max_length=16),
        ),
        migrations.AlterField(
            model_name='tage',
            name='metraj',
            field=models.IntegerField(blank=True, default='120'),
        ),
        migrations.AlterField(
            model_name='tage',
            name='vazn',
            field=models.IntegerField(blank=True),
        ),
        migrations.AddField(
            model_name='factorforoosh',
            name='kharidar',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(factor0.models), to='customer0.moshtary'),
        ),
    ]