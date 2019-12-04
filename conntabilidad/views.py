from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from conntabilidad.forms import PagoForm
from conntabilidad.models import Pago
from CEM.models import Doctor
from django.db.models import *
from datetime import datetime

#### Para reporte #####
from io import BytesIO
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
















########################## Resporte contable de ingresos ##############################

def reporteContable(request):
    #suma = Pago.objects.all().aggregate(s = Sum('montoPago'))
    #valor = suma['s']
    cursor = connection.cursor()
    cursor.execute(" select SUM(p.\"montoPago\") as suma from conntabilidad_pago as p where TO_DATE(to_char(p.\"fechaPago\",'YYYY-MM-DD'),'YYYY-MM-DD') = current_date ")
    lista = cursor.fetchall()
    l = lista[0]
    valor =  l[0]
    
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer,
                            pagesize=letter,
                            title="Reporte de Ingresos",
                                )

    style = getSampleStyleSheet()

    versuma = Paragraph('Total de Ingresos: '+str(valor),style['Heading3'])
    elementos = []
    img1 = Image(0,0,200,60,"CEM/imagenes/logo.PNG")
    dibujo = Drawing(30,30)
    dibujo.add(img1)

    titulo = Paragraph('Reporte de Ingresos', style['Heading1'])
     #table
    encabezados = ('                             Doctor','','Monto')
    #info_tabla = [(pago.idDoctor, pago.montoPago) for pago in Pago.objects.all()]
    #2da alternativa
    cursor2 = connection.cursor()
    cursor2.execute(" select d.\"primerNombreDoctor\",d.\"primerApellidoDoctor\",SUM(p.\"montoPago\") as total from \"CEM_doctor\" as d inner join conntabilidad_pago as p on d.id = p.\"idDoctor_id\" where TO_DATE(to_char(p.\"fechaPago\",'YYYY-MM-DD'),'YYYY-MM-DD') = current_date group by d.\"primerApellidoDoctor\",d.\"primerNombreDoctor\"  ")
    info_tabla = cursor2.fetchall()
    tabla = Table([encabezados]+ info_tabla, colWidths=[100,100,150]) 
    tabla.setStyle(TableStyle(
            [
            ('GRID', (0, 0), (3, -1), 0.5, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
            ]
        ))
    """p=0   
    for i in Pago.objects.all():
        p = p + i.montoPago
    versuma = Paragraph(str(p),style['BodyText'])"""

    elementos.append(dibujo)
    elementos.append(titulo)
    elementos.append(Spacer(0,15) )
    elementos.append(tabla)
    elementos.append(Spacer(0,15) )
    elementos.append(versuma)
    pdf.build(elementos)
    response.write(buffer.getvalue())
    buffer.close()  
    return response 


















