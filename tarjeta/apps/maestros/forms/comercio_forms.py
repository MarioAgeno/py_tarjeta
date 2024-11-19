# tarjeta\apps\maestros\forms\comercio_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import *
from ..models.comercio_models import Comercio
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect, formclasscheck)


class ComercioForm(CrudGenericForm):
	
	class Meta:
		model = Comercio
		fields = '__all__'

		widgets = {
			'estatus_comercio': 
				forms.Select(attrs={**formclassselect}), 
			'codigo_comercio': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 99999999}),
			'pin': 
				forms.NumberInput(attrs={**formclasstext, 
							'readonly': True}),
			'razon_social_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'nombre_titular': 
				forms.TextInput(attrs={**formclasstext}),
			'domicilio_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_provincia': 
				forms.Select(attrs={**formclassselect}), 
			'id_localidad': 
				forms.Select(attrs={**formclassselect}), 
			'telefono_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono2_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'movil_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'mail_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_actividad': 
				forms.Select(attrs={**formclassselect}), 
			'id_sucursal': 
				forms.Select(attrs={**formclassselect}), 
			'codigo_socio': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 99999}),
			'id_tipo_iva': 
				forms.Select(attrs={**formclassselect}), 
			'cuit_comercio':
				forms.NumberInput(attrs={**formclasstext}),
			'ingreso_bruto': 
				forms.TextInput(attrs={**formclasstext}),
			'monto_fijo': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'exento_ganancias': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'estacion_servicio': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'debito_credito': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'acreditar_cuenta': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'leido': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'mensaje': 
				forms.TextInput(attrs={**formclasstext}),
			'porcentaje_consumo': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'porcentaje_retencion_ib': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Verifica si estamos editando un registro con provincia ya seleccionada
		if self.instance and self.instance.pk and self.instance.id_provincia:

			localidades = Localidad.objects.filter(id_provincia=self.instance.id_provincia).order_by('nombre_localidad')

			# Configura el campo para mostrar 'nombre_localidad - codigo_postal'
			self.fields['id_localidad'].choices = [
				(loc.id_localidad, f"{loc.nombre_localidad} - {loc.codigo_postal}")
				for loc in localidades
			]
   
		else:
			# En caso de nuevo registro o provincia no seleccionada, muestra un queryset vacío
			# self.fields['id_localidad'].queryset = Localidad.objects.none()
			self.fields['id_localidad'].choices = []
			
		# Opcional: si quieres que se muestre un mensaje de "Seleccione una localidad"
		# self.fields['id_localidad'].empty_label = "Seleccione una localidad"
		self.fields['id_localidad'].empty_label = "Seleccione una localidad"
		
