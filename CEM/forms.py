from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .validators import validate_email
from .models import Doctor, Paciente, Consulta

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('user','primerNombreDoctor', 'segundoNombreDoctor', 'primerApellidoDoctor', 'segundoApellidoDoctor', 'especialidad', 'sexoDoctor', 'fechaNacimientoDoctor',
        'telefonoDoctor', 'correoElectronico', 'duiDoctor', 'nitDoctor', 'ncfDoctor', 'fotografiaDoctor', )
        widgets = {
            'fechaNacimientoDoctor' : DatePickerInput(format='%d/%m/%Y'),
            'nitDoctor': forms.TextInput(attrs={'placeholder':'9999-999999-999-9'}),
            'duiDoctor': forms.TextInput(attrs={'placeholder':'99999999-9'}),
            'ncfDoctor': forms.TextInput(attrs={'placeholder':'999999-9'}),
            'telefonoDoctor': forms.TextInput(attrs={'placeholder':'9999-9999'})
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
            'fechaNacimientoPaciente' : DatePickerInput(format='%d/%m/%Y'),
            'alturaPaciente' : forms.TextInput(attrs={'placeholder':'Altura en centimetros'}),
            'pesoPaciente' : forms.TextInput(attrs={'placeholder':'Peso en libras'}),
            'telefonoPaciente' : forms.TextInput(attrs={'placeholder':'9999-9999'})

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