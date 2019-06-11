from django.contrib import admin
from .models import Doctor, Paciente, Consulta
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Consulta)