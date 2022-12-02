from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Recibo
from .forms import ReciboModelForm


class ReciboView(ListView):
    models = Recibo
    template_name = 'recibos.html'
    queryset = Recibo.objects.all()
    context_object_name = 'recibos'


class CreateReciboView(CreateView):
    model = Recibo
    template_name = 'recibo_form.html'
    fields = ['nome', 'saram', 'graduacao', 'setor', 'ramal', 'data', 'especificacoes',
              'observacao', 'sinf', 'lacre', 'bmp', 'quantidade',
              ]
    success_url = reverse_lazy('recibos')
