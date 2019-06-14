from django import forms

from .models import Doctor, Paciente

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('primerNombreDoctor', 'segundoNombreDoctor', 'primerApellidoDoctor', 'segundoApellidoDoctor', 'especialidad', 'sexoDoctor', 'fechaNacimientoDoctor',
        'telefonoDoctor', 'correoElectronico', 'duiDoctor', 'fotografiaDoctor', )

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['fotografiaDoctor'].required = False

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('idDoctor', 'expediente','primerNombrePaciente', 'segundoNombrePaciente', 'primerApellidoPaciente', 'segundoApellidoPaciente', 'sexoPaciente', 'fechaNacimientoPaciente', 
        'alturaPaciente', 'pesoPaciente', 'telefonoPaciente', 'fotografiaPaciente', 'institucion', 'alergias', 'antecedentes', )

    idDoctor = forms.ModelChoiceField(queryset=Doctor.objects.all())

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.fields['fotografiaPaciente'].required = False