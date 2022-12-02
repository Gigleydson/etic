from django.urls import path
from .views import ReciboView, CreateReciboView

urlpatterns = [
    path('recibos/', ReciboView.as_view(), name='recibos'),
    path('adicionar/', CreateReciboView.as_view(), name='adicionar_recibo')
]
