from django.urls import path
from .views import DoctorListView, DoctorDetailView, doctorNuevo, doctorEditar

urlpatterns = [
    path('doctor/<int:pk>/editar/', doctorEditar, name='doctor_editar'),
    path('doctor/nuevo/', doctorNuevo, name='doctor_nuevo'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_datos'),
    path('doctor/list/',DoctorListView.as_view(), name='doctores')
]