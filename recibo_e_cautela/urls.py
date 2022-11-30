from django.urls import path
from .views import ReciboView, ListaReciboView

urlpatterns = [
    path('recibo', ReciboView.as_view(), name='recibo'),
    path('lista_recibo', ListaReciboView.as_view(), name='lista_recibo')
]
