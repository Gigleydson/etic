from django.urls import path
from .views import ReciboView, CreateReciboView, UpdateReciboView, DeleteReciboView, DetailReciboView

urlpatterns = [
    path('recibos/', ReciboView.as_view(), name='recibos'),
    path('adicionar/', CreateReciboView.as_view(), name='adicionar_recibo'),
    path('<int:pk>/update/', UpdateReciboView.as_view(), name='update_recibo'),
    path('<int:pk>/delete/', DeleteReciboView.as_view(), name='delete_recibo'),
    path('<int:pk>/detail/', DetailReciboView.as_view(), name='detail_recibo')
]
