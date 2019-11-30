from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from conntabilidad.forms import PagoForm
from conntabilidad.models import Pago
from CEM.models import Doctor
from django.db.models import *
from datetime import datetime

def pagos(request):
    query = None
    if request.GET:
        query = request.GET['q']
        query = str(query)
    if query != None :
        pagos = get_pago_queryset(query)
    else :
        pagos = Pago.objects.all()
    return render(request, 'conta/pagos.html', {'pagos':pagos})

def pagosDiario(request):
    sumatoria = 0
    doctores = Doctor.objects.none()
    pagoDoctores = {}
    pagosDiarios = Pago.objects.filter(
        Q(fechaPago__day = datetime.now().day) &
        Q(fechaPago__month = datetime.now().month) &
        Q(fechaPago__year = datetime.now().year)
    ).distinct()

    for pago in pagosDiarios:
        sumatoria += pago.montoPago
        doctores |= Doctor.objects.filter(primerApellidoDoctor = pago.idDoctor)

    for doctor in doctores:
        sumaTemp = 0
        for pago in pagosDiarios:
            if str(pago.idDoctor) == str(doctor.primerApellidoDoctor) :
                sumaTemp += pago.montoPago
        pagoDoctores[doctor] = sumaTemp;

    return render(request, 'conta/pagoDiario.html', {'pagosDiarios':pagosDiarios, 'sumatoria':sumatoria, 'doctores':doctores, 'pagoDoctores':pagoDoctores})

def pagoDatos(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    return render(request, 'conta/pagoDato.html', {'pago':pago})

def pagoNuevo(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagos')
    else :
        form = PagoForm()
    return render(request, 'conta/pagoNuevo.html', {'form':form})

def pagoEditar(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == 'POST':
        form = PagoForm(request.POST, instance = pago)
        if form.is_valid:
            pago = form.save()
            pago.save()
            return redirect('pagos')
        else:
            form = PagoForm()
    else :
        form = PagoForm(instance = pago)
    return render(request, 'conta/pagoEditar.html', {'form':form})

def pagoEliminarFuncion(request, pk):
    temp = Pago.objects.get(pk=pk).delete()
    return redirect('pagos')

def get_pago_queryset(query = None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        pagos = Pago.objects.filter(
            Q(fechaPago__month = q)  &
            Q(fechaPago__year = datetime.now().year)
        ).distinct()

        for pago in pagos:
            queryset.append(pago)
    
    return list(set(queryset))