# Generated by Django 4.2.8 on 2023-12-28 10:02

from django.db import migrations, models
import django.db.models.deletion


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
                ('girande', models.CharField(max_length=100)),
                ('zi_naf', models.CharField(max_length=100)),
                ('tarikhe_daryaft', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('tahvil_dahande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer0.moshtary')),
            ],
            options={
                'ordering': ['-shomare_sayad'],
            },
        ),
    ]
