# tarjeta\apps\listados\urls.py
from django.urls import path
from .views.liquidacion_comercio_views import LiquidacionComercioFilterView, LiquidacionComercioPDFView


urlpatterns = [
    path('liquidaciones/filtrar/', LiquidacionComercioFilterView.as_view(), name='liquidaciones-filter'),
    path('liquidaciones/pdf/', LiquidacionComercioPDFView.as_view(), name='liquidacion_pdf'),
]
