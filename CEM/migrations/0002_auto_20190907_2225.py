# Generated by Django 2.1.7 on 2019-09-08 04:25

import CEM.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='correoElectronico',
            field=models.CharField(max_length=50, validators=[CEM.validators.validate_email]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='duiDoctor',
            field=models.CharField(max_length=12, validators=[CEM.validators.validate_dui]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='ncfDoctor',
            field=models.CharField(max_length=15, validators=[CEM.validators.validate_nrc]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='nitDoctor',
            field=models.CharField(max_length=20, validators=[CEM.validators.validate_nit]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='primerApellidoDoctor',
            field=models.CharField(max_length=50, validators=[CEM.validators.validate_apellido]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='primerNombreDoctor',
            field=models.CharField(max_length=50, validators=[CEM.validators.validate_nombre]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='segundoApellidoDoctor',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[CEM.validators.validate_apellido]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='segundoNombreDoctor',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[CEM.validators.validate_nombre]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='telefonoDoctor',
            field=models.CharField(max_length=9, validators=[CEM.validators.validate_telefono]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='primerApellidoPaciente',
            field=models.CharField(max_length=50, validators=[CEM.validators.validate_apellido]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='primerNombrePaciente',
            field=models.CharField(max_length=50, validators=[CEM.validators.validate_nombre]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='segundoApellidoPaciente',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[CEM.validators.validate_apellido]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='segundoNombrePaciente',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[CEM.validators.validate_nombre]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefonoPaciente',
            field=models.CharField(blank=True, max_length=9, null=True, validators=[CEM.validators.validate_telefono]),
        ),
    ]