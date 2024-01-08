# Generated by Django 5.0 on 2024-01-08 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer0', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daftar', models.IntegerField()),
                ('shomare_sayad', models.CharField(max_length=16)),
                ('tarikh', models.CharField(max_length=15)),
                ('mablag', models.CharField(max_length=20)),
                ('kode_meli', models.CharField(max_length=20)),
                ('magsad', models.CharField(blank=True, max_length=100, null=True)),
                ('tarikhe_daryaft', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('ki_daryaft_kard', models.CharField(blank=True, max_length=100, null=True)),
                ('tahvil_dahande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer0.moshtary')),
            ],
            options={
                'ordering': ['-daftar'],
            },
        ),
        migrations.CreateModel(
            name='Daryafti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nagdi', models.IntegerField(blank=True, null=True)),
                ('tarikhe_daryaft', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('chek', models.ManyToManyField(blank=True, to='chek0.chek')),
            ],
        ),
    ]
