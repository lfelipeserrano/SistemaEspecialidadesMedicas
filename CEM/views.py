from django.shortcuts import render
from django.views.generic import ListView

from .models import Doctor
# Create your views here.
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctores.html'