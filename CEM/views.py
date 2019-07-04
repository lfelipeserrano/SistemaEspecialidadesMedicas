from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.db.models import Q
import cloudinary
import cloudinary.uploader
import cloudinary.api

from .models import Doctor, Paciente, Consulta
from .forms import DoctorForm, PacienteForm, ConsultaForm
# Create your views here.

cloudinary.config(
    cloud_name = "cemproject", 
    api_key = "385198511276985", 
    api_secret = "rQM7FyLe2hlX0LZC0H9yR3Nkm1o" 
)

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
    usuarios = User.objects.all()
    grupos = Group.objects.all()
    return render(request, 'usuarios.html', {'usuarios':usuarios, 'grupos':grupos})

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
            paciente.save()
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

# def get_doctorPaciente_queryset(query=None):
#     queryset = []
#     queries = query.split(" ")
#     for q in queries:
#         doctorPaciente = paciente.doctores.filter(
#             Q(doctor_id__icontains=q)
#         ).distinct()
    
#     for doctor in doctorPaciente:
#         queryset.append(doctor)

#     return  list(set(queryset))