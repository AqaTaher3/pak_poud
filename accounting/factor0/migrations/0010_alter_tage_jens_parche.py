# Generated by Django 4.2.8 on 2023-12-31 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factor0', '0009_alter_factorforoosh_fee_alter_tage_metraj_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tage',
            name='jens_parche',
            field=models.CharField(default='nil', max_length=16),
        ),
    ]
