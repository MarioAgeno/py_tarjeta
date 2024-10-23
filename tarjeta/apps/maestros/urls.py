# tarjeta\apps\maestros\urls.py
from django.urls import path

#-- Tablas
from .views.actividad_views import *
from .views.provincia_views import *
from .views.localidad_views import *
from .views.tipo_documento_identidad_views import *
from .views.tipo_iva_views import *

#-- Catálogos

urlpatterns = [
	#-- Tablas:
	#-- Actividad.
	path('actividad/', ActividadListView.as_view(), name='actividad_list'),
	path('actividad/nueva/', ActividadCreateView.as_view(), name='actividad_create'),
	path('actividad/<int:pk>/editar/', ActividadUpdateView.as_view(), name='actividad_update'),
	path('actividad/<int:pk>/eliminar/', ActividadDeleteView.as_view(), name='actividad_delete'),
	
	#-- Provincia.
	path('provincia/', ProvinciaListView.as_view(), name='provincia_list'),
	path('provincia/nueva/', ProvinciaCreateView.as_view(), name='provincia_create'),
	path('provincia/<int:pk>/editar/', ProvinciaUpdateView.as_view(), name='provincia_update'),
	path('provincia/<int:pk>/eliminar/', ProvinciaDeleteView.as_view(), name='provincia_delete'),
	
	#-- Localidad.
	path('localidad/', LocalidadListView.as_view(), name='localidad_list'),
	path('localidad/nueva/', LocalidadCreateView.as_view(), name='localidad_create'),
	path('localidad/<int:pk>/editar/', LocalidadUpdateView.as_view(), name='localidad_update'),
	path('localidad/<int:pk>/eliminar/', LocalidadDeleteView.as_view(), name='localidad_delete'),

	#-- TipoDocumentoIdentidad.
	path('tipo_documento_identidad/', TipoDocumentoIdentidadListView.as_view(), name='tipo_documento_identidad_list'),
	path('tipo_documento_identidad/nueva/', TipoDocumentoIdentidadCreateView.as_view(), name='tipo_documento_identidad_create'),
	path('tipo_documento_identidad/<int:pk>/editar/', TipoDocumentoIdentidadUpdateView.as_view(), name='tipo_documento_identidad_update'),
	path('tipo_documento_identidad/<int:pk>/eliminar/', TipoDocumentoIdentidadDeleteView.as_view(), name='tipo_documento_identidad_delete'),
	
	#-- TipoIva.
	path('tipo_iva/', TipoIvaListView.as_view(), name='tipo_iva_list'),
	path('tipo_iva/nueva/', TipoIvaCreateView.as_view(), name='tipo_iva_create'),
	path('tipo_iva/<int:pk>/editar/', TipoIvaUpdateView.as_view(), name='tipo_iva_update'),
	path('tipo_iva/<int:pk>/eliminar/', TipoIvaDeleteView.as_view(), name='tipo_iva_delete'),

]