from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin

from .views import *

urlpatterns = [
    path('logout/', logout_view, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('permisoDenegado/', permisoDenegado, name='permisos'),

    #URL Usuarios
    path('nuevoUsuario/', signup, name='signup'),
    path('usuario/list/', usuarios, name='usuarios'),
    path('usuario/<int:pk>/', usuarioDatos, name='usuario_datos'),
    path('usuario/<int:pk>/editar/', usuarioEditar, name='usuario_editar'),
    path('usuario/<int:pk>/eliminar/', usuarioEliminar, name='usuario_eliminar'),
    #URL Consulta
    # path('consulta/', consultaInicio.as_view(), name='consulta'),
    path('consulta/<int:pk>/eliminar/', consultaEliminarFuncion, name='consulta_eliminar'),
    path('consulta/<int:pk>/editar', consultaEditar, name='consulta_editar'),
    path('consulta/nuevo/', consultaNuevo, name='consulta_nuevo'),
    path('consulta/list/', consultas, name='consultas'),
    path('consulta/<int:pk>/', consultaDatos, name='consulta_datos'),

    #URL Paciente
    # path('paciente/', pacienteInicio.as_view(), name='paciente'),
    path('paciente/<str:pk>/eliminar', pacienteEliminarFuncion, name='paciente_eliminar'),
    path('paciente/<str:pk>/editar/', pacienteEditar, name='paciente_editar'),
    path('paciente/nuevo/', pacienteNuevo, name='paciente_nuevo'),
    path('paciente/list/', pacientes, name='pacientes'),
    path('paciente/<str:pk>/', pacienteDatos, name='paciente_datos'),
    path('paciente/reportePacientes/<str:pk>/', reportePacientes, name='reportePac'), #reporte paciente

    #URL Doctor
    # path('doctor/', doctorInicio.as_view(), name='doctor'),
    path('doctor/<int:pk>/eliminar/', doctorEliminarFuncion, name='doctor_eliminar'),
    path('doctor/<int:pk>/editar/', doctorEditar, name='doctor_editar'),
    path('doctor/nuevo/', doctorNuevo, name='doctor_nuevo'),
    path('doctor/<int:pk>/', doctorDatos, name='doctor_datos'),
    path('doctor/list/', doctores, name='doctores'),
    path('doctor/reporteDoctores/<int:pk>/', reporteDoctores, name='reporteDoc'), #Reporte doctor

    path('', inicio.as_view(), name='inicio')
]