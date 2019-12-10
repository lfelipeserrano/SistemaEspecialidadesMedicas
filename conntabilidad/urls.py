from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *
from . import views
from CEM.views import permisoDenegado

urlpatterns = [
    path('conta/pago/<int:pk>/eliminar', pagoEliminarFuncion, name='pago_eliminar'),
    path('conta/pago/<int:pk>/editar', pagoEditar, name='pago_editar'),
    path('conta/pago/nuevo/', pagoNuevo, name='pago_nuevo'),
    path('conta/pago/list/', pagos, name='pagos'),
    path('conta/pago/<int:pk>/', pagoDatos, name='pago_datos'),
    path('cotna/pago/pagoDiario/', pagosDiario, name='pago_diario'),



    path('conta/reporteIngresos', reporteContable, name='reporteContable')
]