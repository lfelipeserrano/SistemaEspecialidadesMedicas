from django.db import models
from CEM.models import Doctor
from datetime import datetime

class Pago(models.Model):
    idDoctor = models.ForeignKey(
      Doctor,
      on_delete= models.SET_NULL,
      null= True
    )
    montoPago = models.FloatField()
    fechaPago = models.DateTimeField(default = datetime.now())
