from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Doctor, Paciente, Consulta

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('primerNombreDoctor', 'segundoNombreDoctor', 'primerApellidoDoctor', 'segundoApellidoDoctor', 'especialidad', 'sexoDoctor', 'fechaNacimientoDoctor',
        'telefonoDoctor', 'correoElectronico', 'duiDoctor', 'nitDoctor', 'ncfDoctor', 'fotografiaDoctor', )
        widgets = {
            'fechaNacimientoDoctor' : DatePickerInput(format='%d/%m/%Y')
        }

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['fotografiaDoctor'].required = False

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('doctores', 'expediente','primerNombrePaciente', 'segundoNombrePaciente', 'primerApellidoPaciente', 'segundoApellidoPaciente', 'sexoPaciente', 'fechaNacimientoPaciente', 
        'alturaPaciente', 'pesoPaciente', 'telefonoPaciente', 'fotografiaPaciente', 'institucion', 'aseguradora', 'alergias', 'lugarProveniencia', 'tabquista', 'etilista',
        'hipertenso', 'diabetico', 'tuberculosis', 'anemia', 'convulsiones', 'convulsiones', 'cancer', 'lugarCancer', 'tratamientoCancer', 'antecedentes', )
        widgets = {
            'fechaNacimientoPaciente' : DatePickerInput(format='%d/%m/%Y')
        }

    # idDoctor = forms.ModelChoiceField(queryset=Doctor.objects.all())

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.fields['fotografiaPaciente'].required = False

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('idDoctor', 'expediente', 'fechaConsulta', 'pesoConsulta', 'presionConsulta', 'temperatura', 'pulso', 'alturaConsulta', 'observaciones', 'recetas', 'examenesSolicitados',
            'reporteExamenes', 'fechaUltimaRegla', )
        widgets = {
            'fechaConsulta' : DatePickerInput(format='%d/%m/%Y')
        }