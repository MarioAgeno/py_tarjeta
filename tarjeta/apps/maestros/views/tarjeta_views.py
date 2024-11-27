# tarjeta\apps\maestros\views\tarjeta_views.py
from django.urls import reverse_lazy
from ..views.cruds_views_generics import *
from ..models.tarjeta_models import Tarjeta
from ..forms.tarjeta_forms  import TarjetaForm
#from django.core.exceptions import ValidationError
#from django.db import IntegrityError
from utils.validatos.validaciones import calcular_digito_tarjeta

class ConfigViews():
	# Modelo
	model = Tarjeta
	
	# Formulario asociado al modelo
	form_class = TarjetaForm
	
	# Aplicación asociada al modelo
	app_label = model._meta.app_label
	
	#-- Deshabilitado por redundancia:
	# # Título del listado del modelo
	# master_title = model._meta.verbose_name_plural
	
	#-- Usar esta forma cuando el modelo esté compuesto de una sola palabra: Ej. Color.
	model_string = model.__name__.lower()  #-- Usar esta forma cuando el modelo esté compuesto de una sola palabra: Ej. Color.
	
	#-- Usar esta forma cuando el modelo esté compuesto por más de una palabra: Ej. TipoCambio colocar "tipo_cambio".
	#model_string = "tipo_cambio"
	
	# Permisos
	permission_add = f"{app_label}.add_{model_string}"
	permission_change = f"{app_label}.change_{model_string}"
	permission_delete = f"{app_label}.delete_{model_string}"
	
	# Vistas del CRUD del modelo
	list_view_name = f"{model_string}_list"
	create_view_name = f"{model_string}_create"
	update_view_name = f"{model_string}_update"
	delete_view_name = f"{model_string}_delete"
	
	# Plantilla para crear o actualizar el modelo
	template_form = f"{app_label}/{model_string}_form.html"
	
	# Plantilla para confirmar eliminación de un registro
	template_delete = "base_confirm_delete.html"
	
	# Plantilla de la lista del CRUD
	template_list = f'{app_label}/maestro_list.html'
	
	# Contexto de los datos de la lista
	context_object_name	= 'objetos'
	
	# Vista del home del proyecto
	home_view_name = "home"
	
	# Nombre de la url 
	success_url = reverse_lazy(list_view_name)


class DataViewList():
	search_fields = ['nombre_titular', 'numero_tarjeta']

	ordering = ['nombre_titular']
	
	paginate_by = 8
	  
	table_headers = {
		'estatus_tarjeta': (1, 'Numero'),
		'numero_tarjeta': (2, 'Numero'),
		'nombre_titular': (3, 'Titular'),
		'codigo_socio': (2, 'Socio'),
		'id_localidad': (2, 'Localidad'),
		'acciones': (2, 'Acciones'),
	}
	
	table_data = [
		{'field_name': 'estatus_tarjeta', 'date_format': None},
		{'field_name': 'numero_tarjeta', 'date_format': None},
		{'field_name': 'nombre_titular', 'date_format': None},
		{'field_name': 'codigo_socio', 'date_format': None},
		{'field_name': 'id_localidad', 'date_format': None},
	]


# TarjetaListView - Inicio
class TarjetaListView(MaestroListView):
	model = ConfigViews.model
	template_name = ConfigViews.template_list
	context_object_name = ConfigViews.context_object_name
	
	search_fields = DataViewList.search_fields
	ordering = DataViewList.ordering
	
	extra_context = {
		"master_title": ConfigViews.model._meta.verbose_name_plural,
		"home_view_name": ConfigViews.home_view_name,
		"list_view_name": ConfigViews.list_view_name,
		"create_view_name": ConfigViews.create_view_name,
		"update_view_name": ConfigViews.update_view_name,
		"delete_view_name": ConfigViews.delete_view_name,
		"table_headers": DataViewList.table_headers,
		"table_data": DataViewList.table_data,
	}


# TarjetaCreateView - Inicio
class TarjetaCreateView(MaestroCreateView):
	model = ConfigViews.model
	list_view_name = ConfigViews.list_view_name
	form_class = ConfigViews.form_class
	template_name = ConfigViews.template_form
	success_url = ConfigViews.success_url
	
	#-- Indicar el permiso que requiere para ejecutar la acción.
	# (revisar de donde lo copiaste que tienes asignado permission_change en vez de permission_add)
	permission_required = ConfigViews.permission_add

	def get_initial(self):
		initial = super().get_initial()
		#-- Asignar la sucursal del usuario autenticado como valor inicial.
		initial['id_sucursal'] = self.request.user.id_sucursal
		return initial

	def form_valid(self, form):
        # Calcular el número de tarjeta
		numero_tarjeta = calcular_digito_tarjeta(
            form.instance.id_sucursal.id_sucursal, 
            form.instance.codigo_socio, 
            form.instance.adicional
        )
        
        # Verificar si el número ya existe
		if Tarjeta.objects.filter(numero_tarjeta=numero_tarjeta).exists():
			form.add_error('numero_tarjeta', "El número de tarjeta ya existe. Por favor, verifica los datos ingresados.")  # Especifica el campo
			return self.form_invalid(form)

        # Asignar valores al formulario
		form.instance.numero_tarjeta = numero_tarjeta
		form.instance.digito_verificador = numero_tarjeta % 10
		form.instance.saldo_disponible = form.instance.limite_maximo_tarjeta

		return super().form_valid(form)  # Guardar si todo está bien

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['accion'] = f"Crear {self.model._meta.verbose_name}"
		return context


# TarjetaUpdateView
class TarjetaUpdateView(MaestroUpdateView):
	model = ConfigViews.model
	list_view_name = ConfigViews.list_view_name
	form_class = ConfigViews.form_class
	template_name = ConfigViews.template_form
	success_url = ConfigViews.success_url
	
	#-- Indicar el permiso que requiere para ejecutar la acción.
	permission_required = ConfigViews.permission_change
	
	extra_context = {
		"accion": f"Editar {ConfigViews.model._meta.verbose_name}",
		"list_view_name" : ConfigViews.list_view_name
	}


# TarjetaDeleteView
class TarjetaDeleteView (MaestroDeleteView):
	model = ConfigViews.model
	list_view_name = ConfigViews.list_view_name
	template_name = ConfigViews.template_delete
	success_url = ConfigViews.success_url
	
	#-- Indicar el permiso que requiere para ejecutar la acción.
	permission_required = ConfigViews.permission_delete
	
	extra_context = {
		"accion": f"Eliminar {ConfigViews.model._meta.verbose_name}",
		"list_view_name" : ConfigViews.list_view_name,
		"mensaje": "Estás seguro de eliminar el Registro"
	}
