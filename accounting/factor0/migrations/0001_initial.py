# Generated by Django 5.0 on 2024-01-09 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chek0', '0001_initial'),
        ('customer0', '0002_alter_client_options_alter_recipient_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(default='nil-bangal', max_length=16)),
                ('dyeing', models.CharField(default='sooper_derakhshan', max_length=30)),
                ('weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('meter', models.DecimalField(decimal_places=3, default=120, max_digits=6, null=True)),
            ],
            options={
                'verbose_name_plural': 'Rolls',
                'ordering': ['-material', '-weight', '-meter'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor_number', models.IntegerField(blank=True, default=2000, null=True)),
                ('geymat', models.DecimalField(decimal_places=3, default=240, max_digits=6, null=True)),
                ('selling_date', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('daryafti', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chek0.received')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer0.client')),
                ('roll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factor0.roll')),
            ],
            options={
                'verbose_name_plural': 'Invoices',
                'ordering': ['-factor_number'],
            },
        ),
    ]
