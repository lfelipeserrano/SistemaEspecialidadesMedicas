from django.urls import path
from .views import doctores, doctorDatos, doctorNuevo, doctorEditar, DoctorEliminar, pacienteDatos, pacientes, pacienteNuevo

urlpatterns = [
    path('paciente/nuevo/', pacienteNuevo, name='paciente_nuevo'),
    path('paciente/list/', pacientes, name='pacientes'),
    path('paciente/<str:pk>/', pacienteDatos, name='paciente_datos'),
    path('doctor/<int:pk>/eliminar/', DoctorEliminar.as_view(), name='doctor_eliminar'),
    path('doctor/<int:pk>/editar/', doctorEditar, name='doctor_editar'),
    path('doctor/nuevo/', doctorNuevo, name='doctor_nuevo'),
    path('doctor/<int:pk>/', doctorDatos, name='doctor_datos'),
    path('doctor/list/', doctores, name='doctores')
]