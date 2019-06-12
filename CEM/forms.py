from django import forms

from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('primerNombreDoctor', 'segundoNombreDoctor', 'primerApellidoDoctor', 'segundoApellidoDoctor', 'especialidad', 'sexoDoctor', 'fechaNacimientoDoctor',
        'telefonoDoctor', 'correoElectronico', 'duiDoctor', 'fotografiaDoctor', )

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['fotografiaDoctor'].required = False