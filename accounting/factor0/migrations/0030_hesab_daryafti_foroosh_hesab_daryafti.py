# Generated by Django 5.0 on 2024-01-07 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chek0', '0003_alter_chek_options'),
        ('factor0', '0029_foroosh_baste_shod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hesab_daryafti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nagdi', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('tarikhe_daryaft', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('chek', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chek0.chek')),
                ('daftari', models.ManyToManyField(blank=True, to='factor0.tage')),
            ],
        ),
        migrations.AddField(
            model_name='foroosh',
            name='Hesab_daryafti',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factor0.hesab_daryafti'),
        ),
    ]
