# Generated by Django 5.0 on 2024-01-11 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factor0', '0003_invoice_remaining'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='remaining',
        ),
    ]
