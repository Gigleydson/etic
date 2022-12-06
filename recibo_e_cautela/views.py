from django.views.generic import ListView, DetailView
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
    form_class = ReciboModelForm
    success_url = reverse_lazy('recibos')


class UpdateReciboView(UpdateView):
    model = Recibo
    template_name = 'recibo_form.html'
    form_class = ReciboModelForm
    success_url = reverse_lazy('recibos')


class DeleteReciboView(DeleteView):
    model = Recibo
    template_name = 'recibo_delete.html'
    success_url = reverse_lazy('recibos')


class DetailReciboView(DetailView):
    models = Recibo
    template_name = 'recibo_detail.html'
    queryset = Recibo.objects
    context_object_name = 'recibo'
