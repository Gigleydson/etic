from django import forms
import datetime


class ReciboForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    saram = forms.CharField(label='Saram', max_length=7)
    graduacao = forms.CharField(label='Posto / Graduação', max_length=100)
    setor = forms.CharField(label='Setor / Seção', max_length=100)
    ramal = forms.CharField(label='Ramal', max_length=4)
    data = forms.DateField(label='Data', default=datetime.date.today())
    especificacoes = forms.CharField(label='Especifiações', widget=forms.Textarea())
    observacao = forms.CharField(label='Observações', widget=forms.Textarea())
    sinf = forms.CharField(label='SINF', max_length=4)
    lacre = forms.CharField(label='Lacre', max_length=7)
    bmp = forms.CharField(label='BMP', max_length=10)
    quantidade = forms.CharField(label='Quantidade', max_length=100)
