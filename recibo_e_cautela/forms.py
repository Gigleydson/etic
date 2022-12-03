from django import forms
from .models import Recibo
from bootstrap_datepicker_plus.widgets import DatePickerInput


class ReciboModelForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = '__all__'
