from django import forms
from conntabilidad.models import *

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ('idDoctor', 'montoPago', )

    def __init__(self, *args, **kwargs):
        super(PagoForm, self).__init__(*args, **kwargs)