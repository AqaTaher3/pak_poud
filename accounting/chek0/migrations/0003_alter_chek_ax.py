# Generated by Django 5.0 on 2024-01-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chek0', '0002_chek_ax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chek',
            name='ax',
            field=models.ImageField(blank=True, null=True, upload_to='chekha'),
        ),
    ]