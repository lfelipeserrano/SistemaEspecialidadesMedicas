from django.shortcuts import render, redirect
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

