# Generated by Django 4.2.8 on 2023-12-31 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factor0', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tage',
            name='metraj',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='tage',
            name='vazn',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
