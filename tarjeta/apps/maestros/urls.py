# tarjeta\apps\maestros\urls.py
from django.urls import path

#-- Tablas
from .views.actividad_views import *
from .views.provincia_views import *
from .views.localidad_views import *
from .views.tipo_documento_identidad_views import *
from .views.tipo_iva_views import *
from .views.sucursal_views import *
from .views.plan_views import *
from .views.empresa_views import *
from .views.numero_views import *
from .views.parametro_views import *
from .views.tarjeta_estado_views import *
from .views.titulo_views import *
from .views.plan_comercio_views import *
from .views.comercio_views import *
from .views.socio_views import *


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

	#-- Sucursal.
	path('sucursal/', SucursalListView.as_view(), name='sucursal_list'),
	path('sucursal/nueva/', SucursalCreateView.as_view(), name='sucursal_create'),
	path('sucursal/<int:pk>/editar/', SucursalUpdateView.as_view(), name='sucursal_update'),
	path('sucursal/<int:pk>/eliminar/', SucursalDeleteView.as_view(), name='sucursal_delete'),
    
	#-- Plan.
	path('plan/', PlanListView.as_view(), name='plan_list'),
	path('plan/nueva/', PlanCreateView.as_view(), name='plan_create'),
	path('plan/<int:pk>/editar/', PlanUpdateView.as_view(), name='plan_update'),
	path('plan/<int:pk>/eliminar/', PlanDeleteView.as_view(), name='plan_delete'),
    
	#-- Empresa.
	path('empresa/', EmpresaListView.as_view(), name='empresa_list'),
	path('empresa/nueva/', EmpresaCreateView.as_view(), name='empresa_create'),
	path('empresa/<int:pk>/editar/', EmpresaUpdateView.as_view(), name='empresa_update'),
	path('empresa/<int:pk>/eliminar/', EmpresaDeleteView.as_view(), name='empresa_delete'),

	#-- Numeros.
	path('numero/', NumeroListView.as_view(), name='numero_list'),
	path('numero/nueva/', NumeroCreateView.as_view(), name='numero_create'),
	path('numero/<int:pk>/editar/', NumeroUpdateView.as_view(), name='numero_update'),
	path('numero/<int:pk>/eliminar/', NumeroDeleteView.as_view(), name='numero_delete'),

	#-- Parametros.
	path('parametro/', ParametroListView.as_view(), name='parametro_list'),
	path('parametro/nueva/', ParametroCreateView.as_view(), name='parametro_create'),
	path('parametro/<int:pk>/editar/', ParametroUpdateView.as_view(), name='parametro_update'),
	path('parametro/<int:pk>/eliminar/', ParametroDeleteView.as_view(), name='parametro_delete'),
    
	#-- Tarjetas Estados.
	path('tarjetaestado/', TarjetaEstadoListView.as_view(), name='tarjeta_estado_list'),
	path('tarjetaestado/nueva/', TarjetaEstadoCreateView.as_view(), name='tarjeta_estado_create'),
	path('tarjetaestado/<int:pk>/editar/', TarjetaEstadoUpdateView.as_view(), name='tarjeta_estado_update'),
	path('tarjetaestado/<int:pk>/eliminar/', TarjetaEstadoDeleteView.as_view(), name='tarjeta_estado_delete'),

	#-- Titulo.
	path('titulo/', TituloListView.as_view(), name='titulo_list'),
	path('titulo/nueva/', TituloCreateView.as_view(), name='titulo_create'),
	path('titulo/<int:pk>/editar/', TituloUpdateView.as_view(), name='titulo_update'),
	path('titulo/<int:pk>/eliminar/', TituloDeleteView.as_view(), name='titulo_delete'),
    
	#-- Comercios.
	path('comercio/', ComercioListView.as_view(), name='comercio_list'),
	path('comercio/nueva/', ComercioCreateView.as_view(), name='comercio_create'),
	path('comercio/<int:pk>/editar/', ComercioUpdateView.as_view(), name='comercio_update'),
	path('comercio/<int:pk>/eliminar/', ComercioDeleteView.as_view(), name='comercio_delete'),

	#-- Socios.
	path('socio/', SocioListView.as_view(), name='socio_list'),
	path('socio/nueva/', SocioCreateView.as_view(), name='socio_create'),
	path('socio/<int:pk>/editar/', SocioUpdateView.as_view(), name='socio_update'),
	path('socio/<int:pk>/eliminar/', SocioDeleteView.as_view(), name='socio_delete'),
    
	#-- Plan Comercios.
	path('plancomercio/', PlanComercioListView.as_view(), name='plan_comercio_list'),
	path('plancomercio/nueva/', PlanComercioCreateView.as_view(), name='plan_comercio_create'),
	path('plancomercio/<int:pk>/editar/', PlanComercioUpdateView.as_view(), name='plan_comercio_update'),
	path('plancomercio/<int:pk>/eliminar/', PlanComercioDeleteView.as_view(), name='plan_comercio_delete'),
]