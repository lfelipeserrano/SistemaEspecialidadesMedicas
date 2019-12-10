from datetime import datetime, date
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import permission_required
import calendar

#### Para reporte #####
from io import BytesIO
import locale
from django.http import HttpResponse
from reportlab.graphics.shapes import Image,Drawing,Line     #capa mas baja
from reportlab.platypus import SimpleDocTemplate,TableStyle
from reportlab.platypus.tables import Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph,Spacer,Flowable
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4, letter, landscape #nueva
from django.db import connection
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT

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

############# REPORTE C M ###################
def reporteCM(request):
    evento = get_object_or_404(Event)
    if evento.idDoctor != None:
        doctor_consulta = Doctor.objects.get(primerApellidoDoctor = evento.idDoctor)
    else:
        doctor_consulta = Doctor.objects.none()
    if evento.expediente != None:
        paciente_consulta = Paciente.objects.get(expediente = evento.expediente)
    else:
        paciente_consulta = Doctor.objects.none()
    ##################################################
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer,
                            pagesize=letter,
                            title = "AVISO DE CITA MEDICA")
    style = getSampleStyleSheet()
    style.add(ParagraphStyle(name='centro', alignment = TA_CENTER ))

    elementos = []
    img = Image(0,0,50,50,"CEM/imagenes/logoleft.png")#alineacion del  logo-> (rigth-moving, top-moving, weigh, heigh,"url")
    img1 = Image(350,0,100,50,"CEM/imagenes/logocem.png")
    img2 = Image(73,30,260,20,"CEM/imagenes/cemtext.jpg")
    img3 = Image(115,5,175,18,"CEM/imagenes/citamedica.jpg")

    dibujo = Drawing(30,30)#margen superior e izquierdo de donde empieza el pdf
    dibujo.add(img)
    dibujo.add(img1)
    dibujo.add(img2)
    dibujo.add(img3)
    elementos.append(dibujo)
            #FORMATO PARA LA FECHA ACTUAL DE LA MAQUINA
    locale.setlocale(locale.LC_ALL, 'es_ES')#genera en espanol  la fecha
    ahora = datetime.now()
    fecha = ahora.strftime("%A %d de %B del %Y")
    move = movText(275,-20,fecha) #move = movText(387,25,fecha)
    elementos.append(move)
            #SE DIBUJA UNA LINEA DEBAJO DE LAS IMAGENES
    line = linea(450,0,0)
    elementos.append(line)
    elementos.append(Spacer(1,10))
            #ORDEN DE VARIABLES SEGUN consultaDatos.html
    pacnom1 = paciente_consulta.primerNombrePaciente
    pacape1 = paciente_consulta.primerApellidoPaciente
    docnom1 = doctor_consulta.primerNombreDoctor
    docape1 = doctor_consulta.primerApellidoDoctor
    titulo = evento.title
    desc =  evento.description
    fstar = evento.start_time
    fend = evento.end_time
                #FORMATO  PARA EL PARRAFO
    styleJ = style['BodyText']
    styleJ.alignment = TA_JUSTIFY
    styleJ.fontSize = 11
    styleJ.fontName="Times-Roman"
    #styleJ.lineHeight= 1
                #PARRAFO CONCATENADO CON VARIABLES
    parrafo = "<br/><br/><br/><b>EL PACIENTE: </b>"+pacnom1+" "+pacape1+"<br/><br/><br/><b>TIENE UNA CITA CON EL DOCTOR: </b>"+docnom1+" "+docape1+"<br/><br/><br/><b>CON TITULO DE: </b> "+titulo+"<br/><br/><br/><b>DETALLADA CON: </b>"+desc+"<br/><br/><br/><b>QUE COMIENZA EN: </b>"+str(fstar)+" <br/><br/><br/><b>Y TERMINA: </b>"+str(fend)

    elementos.append(Paragraph(parrafo ,styleJ))
    elementos.append(Spacer(1,10))

    pdf.build(elementos)
    response.write(buffer.getvalue())
    buffer.close()
    return response

class linea(Flowable):
    def __init__(self,width,height,width2):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.width2 = width2

    def draw(self):
        self.canv.line(self.width,self.height,self.width2,self.height)

class movText(Flowable):
    def __init__(self,x,y,text=""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.text = text

    def draw(self):
        self.canv.drawString(self.x,self.y,self.text)
        ###############################