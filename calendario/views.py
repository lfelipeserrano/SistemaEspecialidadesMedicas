from datetime import datetime, date
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import permission_required
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm
from django.contrib.auth.models import User

# Create your views here.

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        if  self.request.user.groups.all()[0].name == "Doctores" :
            doctores = Doctor.objects.all()
            for doctor in doctores :
                if  doctor.user == self.request.user :
                    html_cal = cal.formatmonth(doctor, withyear=True)
        else :
            html_cal = cal.formatmonth(withyear=True)
            
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@permission_required('calendario.change_event', login_url='permisos')
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'cal/event.html', {'form': form, 'instance' : instance})

@permission_required('calendario.view_event', login_url='permisos')
def eventDetail(request, event_id):
    instance = get_object_or_404(Event, pk=event_id)
    if instance.expediente != None:
        paciente_consulta = Paciente.objects.get(expediente = instance.expediente)
    else :
        paciente_consulta = Doctor.objects.none()
    return render(request, 'cal/eventDetail.html', {'instance':instance, 'paciente_consulta':paciente_consulta})

@permission_required('calendario.delete_event', login_url='permisos')
def eventoEliminar(request, event_id=None):
    temp = Event.objects.get(pk=event_id).delete()
    return redirect('calendar')