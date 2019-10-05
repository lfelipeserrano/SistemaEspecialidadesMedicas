from django.db import models
from datetime import date
from .validators import validate_email,validate_nombre,validate_apellido,validate_telefono,validate_dui,validate_nit,validate_nrc
from django.contrib.auth.models import User


# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = 1)
    primerNombreDoctor = models.CharField(max_length=50, validators=[validate_nombre])
    segundoNombreDoctor = models.CharField(max_length=50, blank = True, null=True,validators=[validate_nombre])
    primerApellidoDoctor = models.CharField(max_length=50,validators=[validate_apellido])
    segundoApellidoDoctor = models.CharField(max_length=50, blank = True, null=True,validators=[validate_apellido])
    especialidad = models.CharField(max_length=50)
    sexoDoctor = models.BooleanField()
    fechaNacimientoDoctor = models.DateField()
    telefonoDoctor = models.CharField(max_length=9,validators=[validate_telefono])
    correoElectronico = models.CharField(max_length=50, validators= [validate_email])
    duiDoctor = models.CharField(max_length = 12,validators=[validate_dui])
    nitDoctor = models.CharField(max_length = 20,validators=[validate_nit])
    ncfDoctor = models.CharField(max_length = 15,validators=[validate_nrc])
    fotografiaDoctor = models.ImageField(upload_to = 'doctores', blank = True, null=True)

    def __str__(self):
        return self.primerApellidoDoctor

class Paciente(models.Model):
    expediente = models.CharField(max_length = 20)
    doctores = models.ManyToManyField(Doctor)
    primerNombrePaciente = models.CharField(max_length=50,validators=[validate_nombre])
    segundoNombrePaciente = models.CharField(max_length=50, blank = True, null =True ,validators=[validate_nombre])
    primerApellidoPaciente = models.CharField(max_length=50,validators=[validate_apellido])
    segundoApellidoPaciente = models.CharField(max_length=50, blank = True, null = True,validators=[validate_apellido])
    sexoPaciente = models.BooleanField()
    fechaNacimientoPaciente = models.DateField()
    alturaPaciente = models.IntegerField(blank = True, null=True)
    pesoPaciente = models.FloatField(max_length=5, blank = True, null=True)
    telefonoPaciente = models.CharField(max_length=9, blank = True, null = True,validators=[validate_telefono])
    fotografiaPaciente = models.ImageField(upload_to = 'cem/imagenes/pacientes/', blank = True, null = True)
    institucion = models.CharField(max_length = 50, blank = True, null = True)
    aseguradora = models.CharField(max_length = 50, blank = True, null = True)
    alergias = models.TextField(max_length = 200, blank = True)
    lugarProveniencia = models.CharField(max_length = 100, blank = True, null = True)
    tabquista = models.BooleanField()
    etilista = models.BooleanField()
    hipertenso = models.BooleanField()
    diabetico = models.BooleanField()
    tuberculosis = models.BooleanField()
    anemia = models.BooleanField()
    convulsiones = models.BooleanField()
    cancer = models.BooleanField()
    lugarCancer = models.CharField(max_length = 50, blank = True, null = True)
    tratamientoCancer = models.CharField(max_length = 100, blank = True, null = True)
    antecedentes = models.TextField(max_length = 200, blank = True)

    def __str__(self):
        return self.expediente

class Consulta(models.Model):
    idDoctor = models.ForeignKey(
        Doctor,
        on_delete = models.SET_NULL,
        null = True
    )
    expediente = models.ForeignKey(
        Paciente,
        on_delete = models.SET_NULL, 
        null = True
    )
    fechaConsulta = models.DateField()
    pesoConsulta = models.IntegerField(blank=True, null= True)
    presionConsulta = models.CharField(max_length = 10, blank = True, null= True)
    temperatura = models.IntegerField(blank = True, null= True)
    pulso = models.IntegerField(blank=True, null= True)
    alturaConsulta = models.IntegerField(blank=True, null= True)
    observaciones = models.TextField(max_length=500)
    recetas = models.TextField(max_length=200, blank=True, null= True)
    examenesSolicitados = models.TextField(max_length=200, blank=True, null= True)
    reporteExamenes = models.TextField(max_length= 200, blank=True, null=True)
    fechaUltimaRegla = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.fechaConsulta.strftime("%d/%m/%Y")