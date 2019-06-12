from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .models import Doctor
from .forms import DoctorForm
# Create your views here.
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctores.html'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctorDatos.html'

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

