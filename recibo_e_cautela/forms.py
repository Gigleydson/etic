from django import forms
from .models import Recibo


class ReciboModelForm(forms.ModelForm):
    model = Recibo
    fields = '__all__'

