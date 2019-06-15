from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Doctor, Paciente
from .forms import DoctorForm, PacienteForm
# Create your views here.

#VISTAS DOCTOR

def doctores(request):
    doctores =  Doctor.objects.all()
    return render(request, 'doctores.html', {'doctores':doctores})

def doctorDatos(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctorDatos.html', {'doctor':doctor})

def doctorNuevo(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctores')
    else:
        form = DoctorForm()
    return render(request, 'doctorNuevo.html', {
        'form': form
    })

def doctorEditar(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance = doctor)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.save()
            return redirect('doctores')
        else:
            form = DoctorForm()
    else:
        form = DoctorForm(instance = doctor)
    return render(request, 'doctorEditar.html', {
        'form': form
    })  

class DoctorEliminar(DeleteView):
    model = Doctor
    template_name = 'doctorDatos.html'
    success_url = reverse_lazy('doctores')

#VISTA PACIENTES
def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes':pacientes})

def pacienteDatos(request, pk):
    paciente  = get_object_or_404(Paciente, pk=pk)
    doctores_paciente = paciente.doctores.all()
    # doctor = get_object_or_404(Doctor, primerApellidoDoctor=paciente.idDoctor)
    return render(request, 'pacienteDato.html', {'paciente':paciente, 'doctores_paciente':doctores_paciente})

def pacienteNuevo(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacienteNuevo.html', {'form':form})

def pacienteEditar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES, instance = paciente)
        if form.is_valid():
            paciente = form.save()
            paciente.save()
            return redirect('pacientes')
        else:
            form = PacienteForm()
    else:
        form = PacienteForm(instance = paciente)
    return render(request, 'pacienteEditar.html', {'form':form})

class PacienteEliminar(DeleteView):
    model = Paciente
    template_name = 'pacienteDato.html'
    success_url = reverse_lazy('pacientes')