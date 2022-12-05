from django import forms
from .models import Recibo


class ReciboModelForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = ['nome', 'saram', 'graduacao', 'setor', 'ramal', 'data', 'especificacoes',
                  'observacao', 'sinf', 'lacre', 'bmp', 'quantidade',
                  ]
        widgets = {
            'data': forms.TextInput(attrs={'type': 'date'}),
            'especificacoes': forms.Textarea(attrs={'rows': '4'}),
            'observacao': forms.Textarea(attrs={'rows': '4'}),
        }
