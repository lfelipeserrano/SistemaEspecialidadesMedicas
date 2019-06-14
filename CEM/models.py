from django.db import models
from datetime import date

# Create your models here.
class Doctor(models.Model):
    idDoctor = models.AutoField(primary_key=True)
    primerNombreDoctor = models.CharField(max_length=50)
    segundoNombreDoctor = models.CharField(max_length=50, blank = True)
    primerApellidoDoctor = models.CharField(max_length=50)
    segundoApellidoDoctor = models.CharField(max_length=50, blank = True)
    especialidad = models.CharField(max_length=50)
    sexoDoctor = models.BooleanField()
    fechaNacimientoDoctor = models.DateField()
    telefonoDoctor = models.CharField(max_length=9)
    correoElectronico = models.CharField(max_length=50)
    duiDoctor = models.CharField(max_length = 12)
    fotografiaDoctor = models.ImageField(upload_to = 'doctores', blank = True)

    def __str__(self):
        return self.primerApellidoDoctor

class Paciente(models.Model):
    expediente = models.CharField(max_length = 20, primary_key = True)
    idDoctor = models.ForeignKey(
        Doctor,
        on_delete = models.CASCADE
    )
    primerNombrePaciente = models.CharField(max_length=50)
    segundoNombrePaciente = models.CharField(max_length=50, blank = True)
    primerApellidoPaciente = models.CharField(max_length=50)
    segundoApellidoPaciente = models.CharField(max_length=50, blank = True)
    sexoPaciente = models.BooleanField()
    fechaNacimientoPaciente = models.DateField()
    alturaPaciente = models.IntegerField(blank = True, null=True)
    pesoPaciente = models.FloatField(max_length=5, blank = True, null=True)
    telefonoPaciente = models.CharField(max_length=9, blank = True)
    fotografiaPaciente = models.ImageField(upload_to = 'cem/imagenes/pacientes/', blank = True)
    institucion = models.CharField(max_length = 50, blank = True)
    alergias = models.TextField(max_length = 200, blank = True)
    antecedentes = models.TextField(max_length = 200, blank = True)

    def __str__(self):
        return self.expediente

class Consulta(models.Model):
    idConsulta = models.AutoField(primary_key=True)
    idDoctor = models.ForeignKey(
        Doctor,
        on_delete = models.CASCADE
    )
    expediente = models.ForeignKey(
        Paciente,
        on_delete = models.CASCADE
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

    def __str__(self):
        return self.fechaConsulta.strftime("%d/%m/%Y")