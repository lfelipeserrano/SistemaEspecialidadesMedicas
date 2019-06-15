from django.urls import path
from .views import doctores, doctorDatos, doctorNuevo, doctorEditar, DoctorEliminar, pacienteDatos, pacientes, pacienteNuevo, pacienteEditar, PacienteEliminar, consultas, consultaDatos, consultaNuevo, consultaEditar, ConsultaEliminar

urlpatterns = [
    #URL 
    path('consulta/<int:pk>/eliminar/', ConsultaEliminar.as_view(), name='consulta_eliminar'),
    path('consulta/<int:pk>/editar', consultaEditar, name='consulta_editar'),
    path('consulta/nuevo/', consultaNuevo, name='consulta_nuevo'),
    path('consulta/list/', consultas, name='consultas'),
    path('consulta/<int:pk>/', consultaDatos, name='consulta_datos'),

    #URL Paciente
    path('paciente/<str:pk>/eliminar', PacienteEliminar.as_view(), name='paciente_eliminar'),
    path('paciente/<str:pk>/editar/', pacienteEditar, name='paciente_editar'),
    path('paciente/nuevo/', pacienteNuevo, name='paciente_nuevo'),
    path('paciente/list/', pacientes, name='pacientes'),
    path('paciente/<str:pk>/', pacienteDatos, name='paciente_datos'),

    #URL Doctor
    path('doctor/<int:pk>/eliminar/', DoctorEliminar.as_view(), name='doctor_eliminar'),
    path('doctor/<int:pk>/editar/', doctorEditar, name='doctor_editar'),
    path('doctor/nuevo/', doctorNuevo, name='doctor_nuevo'),
    path('doctor/<int:pk>/', doctorDatos, name='doctor_datos'),
    path('doctor/list/', doctores, name='doctores')
]