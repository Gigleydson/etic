# from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import Recibo
from .forms import ReciboForm


class ReciboView(FormView):
    template_name = 'recibo.html'
    form_class = ReciboForm
    success_url = reverse_lazy('lista_recibo.html')

    def get_context_data(self, **kwargs):
        context = super(ReciboView, self).get_context_data(**kwargs)
        return context


class ListaReciboView(TemplateView):
    template_name = 'lista_recibo.html'

    def get_context_data(self, **kwargs):
        context = super(ListaReciboView, self).get_context_data(**kwargs)
        context['recibos'] = Recibo.objects.order.all()
        return context
