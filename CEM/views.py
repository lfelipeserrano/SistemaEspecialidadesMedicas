from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required, user_passes_test
from .validators import validate_email
from django.db.models import Q

from .models import Doctor, Paciente, Consulta
from .forms import DoctorForm, PacienteForm, ConsultaForm

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4,letter   
from reportlab.graphics.shapes import Image,Drawing,Line     #capa mas baja
from reportlab.platypus import SimpleDocTemplate,TableStyle,Image
from reportlab.platypus.tables import Table
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Paragraph,Spacer,Flowable
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT, TA_LEFT
import time
from datetime import datetime
from datetime import date
from django.utils.translation import get_language, activate
#from reportlab.platypus import SimpleDocTemplate
#from reportlab.platypus.tables import Table

# Create your views here.

class inicio(TemplateView):
    template_name = 'home.html'

def error_404_view(request, exception):
    return render(request, 'error_404.html')

def permisoDenegado(request):
    return render(request, 'permisos.html')

@permission_required('CEM.add_user', login_url='permisos')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if  request.POST['grupo'] == 'doctor':
                grupo = Group.objects.get(name='Doctores')
                usuario.groups.add(grupo)
            else :
                grupo = Group.objects.get(name='Asistentes')
                usuario.groups.add(grupo)
            # login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'usuarioNuevo.html', {'form': form})

@permission_required('CEM.view_user', login_url='permisos')
def usuarios(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        query = str(query)
    if query != None :
        usuarios = get_usuario_queryset(query)
    else :
        usuarios = User.objects.all()
    grupos = Group.objects.all()
    return render(request, 'usuarios.html', {'usuarios':usuarios, 'grupos':grupos, 'query':query})

@permission_required('CEM.view_user', login_url='permisos')
def usuarioDatos(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    grupos = usuario.groups.all()
    return  render(request, 'usuarioDatos.html', {'usuario':usuario, 'grupos':grupos})

@permission_required('CEM.change_user', login_url='permisos')
def usuarioEditar(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance = usuario)
        if form.is_valid():
            usuarioF = form.save(commit=False)
            if  request.POST['grupo'] == 'doctor':
                usuario.groups.clear()
                grupo = Group.objects.get(name='Doctores')
                usuario.groups.add(grupo)
            else :
                usuario.groups.clear()
                grupo = Group.objects.get(name='Asistentes')
                usuario.groups.add(grupo)
            form.save()
            return redirect('usuarios')
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm(instance = usuario)
    return render(request, 'usuarioEditar.html', {'form':form, 'usuario':usuario})

@permission_required('CEM.change_user', login_url='permisos')
def usuarioEliminar(request, pk):
    temp = User.objects.get(pk=pk).delete()
    return redirect('usuarios')
#VISTAS DOCTOR
class doctorInicio(TemplateView):
    template_name = 'doctorInicio.html'

@permission_required('CEM.view_doctor', login_url='permisos')
def doctores(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        query = str(query)
    if query != None :
        doctores = get_doc_queryset(query)
    else :
        doctores =  Doctor.objects.all()
    especialidades = Doctor.objects.all().distinct('especialidad')
    return render(request, 'doctores.html', {'doctores':doctores, 'especialidades':especialidades, 'query':query})

@permission_required('CEM.view_doctor', login_url='permisos')
def doctorDatos(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctorDatos.html', {'doctor':doctor})

@permission_required('CEM.add_doctor', login_url='permisos')
def doctorNuevo(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            doctorF = form.save(commit=False)
            if request.POST['sexo'] == 'True':
                doctorF.sexoDoctor = True
            else:
                doctorF.sexoDoctor = False
            doctorF.save()
            return redirect('doctores')
    else:
        form = DoctorForm()
    return render(request, 'doctorNuevo.html', {
        'form': form
    })

@permission_required('CEM.change_doctor', login_url='permisos')
def doctorEditar(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance = doctor)
        if form.is_valid():
            doctor = form.save(commit=False)
            if request.POST['sexo'] == 'True':
                doctor.sexoDoctor = True
            else:
                doctor.sexoDoctor = False
            doctor.save()
            return redirect('doctores')
        else:
            form = DoctorForm()
    else:
        form = DoctorForm(instance = doctor)
    return render(request, 'doctorEditar.html', {
        'form': form, 'doctor':doctor
    })  

@permission_required('CEM.delete_doctor', login_url='permisos')
def doctorEliminarFuncion(request, pk):
    temp = Doctor.objects.get(pk=pk).delete()
    return redirect('doctores')

#VISTA PACIENTES
class pacienteInicio(TemplateView):
    template_name = 'pacienteInicio.html'
    
@permission_required('CEM.view_paciente', login_url='permisos')
def pacientes(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        query  = str(query)
    if query !=  None :
        pacientes = get_paciente_queryset(query)
    else :
        pacientes = Paciente.objects.all()
    doctores = Doctor.objects.all()
    return render(request, 'pacientes.html', {'pacientes':pacientes, 'doctores':doctores})

@permission_required('CEM.view_paciente', login_url='permisos')
def pacienteDatos(request, pk):
    paciente  = get_object_or_404(Paciente, pk=pk)
    doctores_paciente = paciente.doctores.all()
    # doctor = get_object_or_404(Doctor, primerApellidoDoctor=paciente.idDoctor)
    return render(request, 'pacienteDato.html', {'paciente':paciente, 'doctores_paciente':doctores_paciente})

@permission_required('CEM.add_paciente', login_url='permisos')
def pacienteNuevo(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES)
        if form.is_valid():
            pacienteF = form.save(commit=False)
            if request.POST['sexo'] == 'True':
                pacienteF.sexoPaciente = True
            else:
                pacienteF.sexoPaciente = False
            form.save()
            return redirect('pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacienteNuevo.html', {'form':form})

@permission_required('CEM.change_paciente', login_url='permisos')
def pacienteEditar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES, instance = paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            if request.POST['sexo'] == 'True':
                paciente.sexoPaciente = True
            else:
                paciente.sexoPaciente = False
            form.save()
            return redirect('pacientes')
        else:
            form = PacienteForm()
    else:
        form = PacienteForm(instance = paciente)
    return render(request, 'pacienteEditar.html', {'form':form, 'paciente':paciente})

@permission_required('CEM.delete_paciente', login_url='permisos')
def pacienteEliminarFuncion(request, pk):
    temp = Paciente.objects.get(pk=pk).delete()
    return redirect('pacientes')

#VISTAS CONSULTAS
class consultaInicio(TemplateView):
    template_name = 'consultaInicio.html'

@permission_required('CEM.view_consulta', login_url='permisos')
def consultas(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        query = str(query)
    if query != None :
        consultas = get_consulta_queryset(query)
    else :
        consultas = Consulta.objects.all()
    doctores = Doctor.objects.all()
    pacientes = Paciente.objects.all()
    return render(request, 'consultas.html', {'consultas':consultas, 'doctores':doctores, 'pacientes':pacientes})

@permission_required('CEM.view_consulta', login_url='permisos')
def consultaDatos(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if consulta.idDoctor != None:
        doctor_consulta = Doctor.objects.get(primerApellidoDoctor = consulta.idDoctor)
    else:
        doctor_consulta = Doctor.objects.none()
    if consulta.expediente != None:
        paciente_consulta = Paciente.objects.get(expediente = consulta.expediente)
    else:
        paciente_consulta = Doctor.objects.none()
    return render(request, 'consultaDato.html', {'consulta':consulta, 'doctor_consulta':doctor_consulta, 'paciente_consulta':paciente_consulta})

@permission_required('CEM.add_consulta', login_url='permisos')
def consultaNuevo(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = ConsultaForm()
    return render(request, 'consultaNuevo.html', {'form':form})

@permission_required('CEM.change_consulta', login_url='permisos')
def consultaEditar(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance = consulta)
        if form.is_valid:
            consulta = form.save()
            consulta.save()
            return redirect('consultas')
        else:
            form = ConsultaForm()
    else:
        form = ConsultaForm(instance = consulta)
    return render(request, 'consultaEditar.html', {'form':form})

@permission_required('CEM.delete_consulta', login_url='permisos')
def consultaEliminarFuncion(request, pk):
    temp = Consulta.objects.get(pk=pk).delete()
    return redirect('consultas')

def logout_view(request):
    logout(request)
    return redirect('inicio')

def get_doc_queryset(query=None):
    queryset =[]
    queries = query.split(" ")
    for q in queries:
        docs = Doctor.objects.filter(
            Q(primerApellidoDoctor__icontains=q) |
            Q(primerNombreDoctor__icontains=q) |
            Q(especialidad__icontains=q)
        ).distinct()
    
        for doc in docs:
            queryset.append(doc)
    
    return list(set(queryset))

def get_paciente_queryset(query=None):
    queryset =[]
    queries = query.split(" ")
    for q in queries:
        pacientes = Paciente.objects.filter(
            Q(primerApellidoPaciente__icontains=q) |
            Q(primerNombrePaciente__icontains=q) |
            Q(expediente__icontains=q) |
            Q(doctores__id__icontains=q)
        ).distinct()
    
        for paciente in pacientes:
            queryset.append(paciente)
    
    return list(set(queryset))

def get_consulta_queryset(query=None):
    queryset =[]
    queries = query.split(" ")
    for q in queries:
        consultas = Consulta.objects.filter(
            Q(fechaConsulta__icontains=q) |
            Q(idDoctor__id__icontains=q)
        ).distinct()
    
        for consulta in consultas:
            queryset.append(consulta)
    
    return list(set(queryset))

def get_usuario_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        usuarios = User.objects.filter(
            Q(username__icontains=q)
        ).distinct()

        for usuario in usuarios:
            queryset.append(usuario)

    return list(set(queryset))

# R E P O R T E S 
"""def reporteDoctor(request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)

        pdf.drawImage("CEM/imagenes/logo.PNG",50,760,width=200,height=50)
        pdf.setFont("Helvetica",20)
        pdf.drawString(230,730,"REPORTE") 
        pdf.setFont("Helvetica",18)
        pdf.drawString(240,712,"Doctores") 

        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response"""

def reporteDoctores(request):#***********************************#
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = SimpleDocTemplate(response,
                                pagesize=letter)

        style = getSampleStyleSheet()
        elementos=[]
        texto1 = Paragraph("Reporte de Doctores",style['Heading1'])
        img = Image(0,0,200,50,"CEM/imagenes/logo.PNG")
        #img.hAlign = 'LEFT'
        dibujo = Drawing(30,30)
        #dibujo.translate(10,10)
        dibujo.add(img)                 #1
        elementos.append(dibujo)
        #dibujo = Drawing(30,30)
        #dibujo.add(Line(400, 50, 510, 50))
        ahora = datetime.now()
        fecha = ahora.strftime("%d/%m/%Y")
        
        move = movText(387,25,fecha)
        elementos.append(move)
     
        elementos.append(texto1)        #3   
        line= linea(450,0)
        elementos.append(line)   
        # story.append(Spacer(0, 20))
        tab = Spacer(1,40)
        elementos.append(tab)
       #table
        encabezados = ('Apellido','Nombre','Especialidad','Telefono','Correo')
        info_tabla = [(doc.primerApellidoDoctor, doc.primerNombreDoctor, doc.especialidad, doc.telefonoDoctor,doc.correoElectronico) for doc in Doctor.objects.all()]
        tabla = Table([encabezados]+ info_tabla, colWidths=[90,90,90,90,125]) 
        
        tabla.setStyle(TableStyle(
            [
            ('GRID', (0, 0), (-1, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
            ]
        ))

        elementos.append(tabla)                 #4
        elementos.append(Spacer(1,40))
        pdf.build(elementos)
        #pdf = canvas.Canvas(buffer, pagesize=A4)
        """pdf.drawImage("CEM/imagenes/logo.PNG",50,760,width=200,height=50)
        pdf.setFont("Helvetica",20)
        pdf.drawString(230,730,"REPORTE") 
        pdf.setFont("Helvetica",18)
        pdf.drawString(240,712,"Doctores")""" 
        #pdf.save()
        #pdf = buffer.getvalue()
        #buffer.close()
        #response.write(pdf)

        return response

def reporteDoctorIncapacidad(request,pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if consulta.idDoctor != None:
        doctor_consulta = Doctor.objects.get(primerApellidoDoctor = consulta.idDoctor)
    else:
        doctor_consulta = Doctor.objects.none()
    if consulta.expediente != None:
        paciente_consulta = Paciente.objects.get(expediente = consulta.expediente)
    else:
        paciente_consulta = Doctor.objects.none()

    ##################################################
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="Prueba.pdf"'
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer,
                            pagesize=letter,
                            title = "Constancia por Incapacidad")

    style = getSampleStyleSheet()
    style.add(ParagraphStyle(name='centro', alignment = TA_CENTER ))

    elementos = []
    img = Image("CEM/imagenes/logo.PNG",width=200, height=50 )
    img.hAlign = 'LEFT'
    
    styleC = style['Heading1']
    styleC.alignment = 1
    t1 = Paragraph("Constancia Medica por Incapacidad",styleC)

    styleC = style['Heading3']
    styleC.alignment = 0
    titulo2 = Paragraph("A quien Corresponda",styleC)

    f = consulta.fechaConsulta
    f2 = f.strftime("%d/%m/%Y")
    nom1P = paciente_consulta.primerNombrePaciente
    ape1P = paciente_consulta.primerApellidoPaciente
    exp = paciente_consulta.expediente
    nom1D = doctor_consulta.primerNombreDoctor
    ape1D = doctor_consulta.primerApellidoDoctor
    especialidad = doctor_consulta.especialidad
    observaciones = consulta.observaciones
    meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    ahora = datetime.now()
    dia = ahora.strftime("%d")
    mes = meses[ahora.month-1]
    anio = ahora.strftime("%Y")

    styleJ = style['BodyText']
    styleJ.alignment = TA_JUSTIFY
    parrafo = "El infrascrito Medico "+ especialidad +" "+ nom1D + " "+ ape1D +" de la Clinica de Especialidades Medicas CEM, por medio de la presente hago constar que el señor(a) <b>" + nom1P + " " + ape1P + "</b> con expediente clinico numero <b>"+exp+"</b> quien presenta: "+ observaciones +" Se le indicó tratamiento y reposo por ___ horas a partir de la presente fecha "+ f2+""
    parrafo2 = "A peticion de la parte interesada y para usos legales que al mismo convengan se extiende la presente en la Ciudad de San Salvador, a los "+ dia  +" dias del mes de "+ mes +" Año "+anio+" "
    
    #line= linea(372,0)
    line = linea(100,0,372)
    styleC = style['Heading4']
    styleC.alignment = 1
    FYS = "Firma y Sello"
    
    elementos.append(img)
    elementos.append(Spacer(1,10))  
    elementos.append(t1)
    elementos.append(Spacer(1,10))
    elementos.append(titulo2)
    elementos.append(Spacer(1,5))
    elementos.append(Paragraph(parrafo ,styleJ))
    elementos.append(Spacer(1,10))
    elementos.append(Paragraph(parrafo2 ,styleJ))

    elementos.append(Spacer(1,70))
    elementos.append(line)
    elementos.append(Paragraph(FYS ,styleC)) 
#   atr1 = Paragraph(Doctor.primerNombreDoctor,style['Heading2'])
    pdf.build(elementos)
    response.write(buffer.getvalue())
    buffer.close()  
    return response


def reporteDoctorConstancia(request,pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if consulta.idDoctor != None:
        doctor_consulta = Doctor.objects.get(primerApellidoDoctor = consulta.idDoctor)
    else:
        doctor_consulta = Doctor.objects.none()
    if consulta.expediente != None:
        paciente_consulta = Paciente.objects.get(expediente = consulta.expediente)
    else:
        paciente_consulta = Doctor.objects.none()

    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'filename="Prueba.pdf"'
    #response['Content-Disposition'] = 'filename="{}"'.format(file_name)
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer,
                            pagesize=letter,
                            title="Constancia Medica",
                            )

    style = getSampleStyleSheet()
    style.add(ParagraphStyle(name='centro', alignment = TA_CENTER ))
    nomApe = paciente_consulta.primerNombrePaciente +" "+ paciente_consulta.primerApellidoPaciente 
    nomApeD = doctor_consulta.primerNombreDoctor +" "+ doctor_consulta.primerApellidoDoctor
    meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    ahora = datetime.now()
    dia = ahora.strftime("%d")
    mesLetra = meses[ahora.month-1]
    mesNumero = ahora.strftime("%m")
    anio = ahora.strftime("%Y")

    elementos = []
    img = Image("CEM/imagenes/logo.PNG",width=200, height=50 )
    img.hAlign = 'LEFT'
    line= linea(5,0,467)

    styleC = style['Heading1']
    styleC.alignment = 1
    t1 = Paragraph("Constancia Medica",styleC) 
    #title = Paragraph('<para align=center><b>Industry Earnings Call Transcripts Report</b></para>',style['Normal'])
    styleJ = style['BodyText']
    styleJ.alignment = TA_JUSTIFY
    parrafo = "Por medio de la presente se hace constar que el Señor(a): <b>"+nomApe+"</b> paso consulta con el Doctor(a) "+ nomApeD + " el dia " + dia +"/"+ mesNumero +"/"+ anio+"."                        
    parrafo2 = "Y para los usos que el interesado estime conveniente, se extiende la presente en la Ciudad de San Salvador a los "+ dia +" dias del mes de "+ mesLetra +" del "+ anio+". "
    styleC = style['Heading3']
    styleC.alignment = 1
    doc = "Dr.(a) "+ nomApeD +" "
    line2 = linea(100,0,372)
    elementos.append(img)
    elementos.append(Spacer(1,20))
    elementos.append(line)
    elementos.append(Spacer(1,20))
    elementos.append(t1)
    elementos.append(Spacer(1,5))
    #elementos.append(title)
    elementos.append(Paragraph(parrafo,styleJ))
    elementos.append(Spacer(1,20))
    elementos.append(Paragraph(parrafo2,styleJ))
    elementos.append(Spacer(1,90))
    elementos.append(line2)
    elementos.append(Paragraph(doc,styleC))
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
