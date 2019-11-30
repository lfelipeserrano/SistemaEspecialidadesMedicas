from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from conntabilidad.forms import PagoForm
from conntabilidad.models import Pago
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

class inicio(TemplateView):
    template_name = 'conta/contabilidad.html'

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
    suma = Pago.objects.all().aggregate(s = Sum('montoPago'))
    valor = suma['s']
    #suma = Pago.objects.all()

    #valor = dict.get('montoPago__sum') 

    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer,
                            pagesize=letter,
                            title="Reporte de Ingresos",
                                )

    style = getSampleStyleSheet()

    versuma = Paragraph('Total de Ingresos: '+str(valor),style['BodyText'])
    elementos = []
    img1 = Image(0,0,200,60,"CEM/imagenes/logo.PNG")
    dibujo = Drawing(30,30)
    dibujo.add(img1)

    titulo = Paragraph('Reporte de Ingresos', style['Heading1'])
     #table
    encabezados = ('Doctor','Pago')
    info_tabla = [(pago.idDoctor, pago.montoPago) for pago in Pago.objects.all()]
    tabla = Table([encabezados]+ info_tabla, colWidths=[120,120]) 
    tabla.setStyle(TableStyle(
            [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
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
    elementos.append(tabla)
    elementos.append(versuma)
    pdf.build(elementos)
    response.write(buffer.getvalue())
    buffer.close()  
    return response 

