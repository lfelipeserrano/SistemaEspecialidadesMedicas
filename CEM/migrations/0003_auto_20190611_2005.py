# Generated by Django 2.1.7 on 2019-06-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEM', '0002_auto_20190611_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='fotografiaDoctor',
            field=models.ImageField(blank=True, upload_to='cem/imagenes/doctores/'),
        ),
    ]
