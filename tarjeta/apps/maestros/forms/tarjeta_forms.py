# tarjeta\apps\maestros\forms\tarjeta_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import *
from ..models.tarjeta_models import Tarjeta
from datetime import datetime

from diseno_base.diseno_bootstrap import (formclassdate,
	formclasstext, formclassselect, formclasscheck)

class TarjetaForm(CrudGenericForm):

	class Meta:
		model = Tarjeta
		fields = '__all__'

		widgets = {
			'estatus_tarjeta': 
				forms.Select(attrs={**formclassselect}), 
			'id_sucursal': 
				forms.Select(attrs={**formclassselect}), 
			'codigo_socio': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 99999}),
			'adicional': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 99}),
			'digito_verificador': 
				forms.NumberInput(attrs={**formclasstext, 'readonly': True}),
			'numero_tarjeta':  
				forms.NumberInput(attrs={**formclasstext, 'readonly': True}), 
			'nombre_titular': 
				forms.TextInput(attrs={**formclasstext}),
			'domicilio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_localidad': 
				forms.Select(attrs={**formclassselect}), 
			'id_provincia': 
				forms.Select(attrs={**formclassselect}), 
			'telefono_tarjeta': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono2_tarjeta': 
				forms.TextInput(attrs={**formclasstext}),
			'movil_tarjeta': 
				forms.TextInput(attrs={**formclasstext}),
			'mail_tarjeta': 
				forms.TextInput(attrs={**formclasstext}),
			'nombre_garantia': 
				forms.TextInput(attrs={**formclasstext}),
			'limite_maximo_tarjeta': 
				forms.NumberInput(attrs={**formclasstext,
                           'min': 0, 'max': 999999999, 'step': '1'}),
			'saldo_disponible': 
				forms.NumberInput(attrs={**formclasstext, 'readonly': True}),
			'id_titulo': 
				forms.Select(attrs={**formclassselect}), 
			'id_tarjeta_estado': 
				forms.Select(attrs={**formclassselect}), 
			'fecha_alta': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'fecha_baja': 
				forms.TextInput(attrs={'type':'date', **formclassdate, 'readonly': True}),
			'vencimiento': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'liquidacion_mail': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'seguro': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'observacion': 
				forms.TextInput(attrs={**formclasstext}),
		}

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)  # Extraer el usuario autenticado
		super().__init__(*args, **kwargs)
		
		self.fields['id_localidad'].choices = []
		
		#-- Verificar si el formulario se llama con datos (POST).
		if self.is_bound:
			#-- Obtener el valor enviado de id_provincia_tarjeta.
			provincia_id = self.data.get('id_provincia')
			localidad_id = self.data.get('id_localidad', '')
			
			if provincia_id:
				#-- Filtrar localidades según la provincia enviada.
				localidades = Localidad.objects.filter(id_provincia=provincia_id).order_by('nombre_localidad')
				self.fields['id_localidad'].choices = [("", "Seleccione una localidad")] + [
					(loc.id_localidad, f"{loc.nombre_localidad} - {loc.codigo_postal}") for loc in localidades
				]
				self.initial['id_localidad'] = localidad_id
			else:
				self.fields['id_localidad'].choices = [("", "Seleccione una localidad")]
			
		#-- Si se está editando un registro existente.
		elif self.instance and self.instance.pk and self.instance.id_provincia:
			localidades = Localidad.objects.filter(id_provincia=self.instance.id_provincia).order_by('nombre_localidad')
			self.fields['id_localidad'].choices = [
				(loc.id_localidad, f"{loc.nombre_localidad} - {loc.codigo_postal}")
				for loc in localidades
			]
			
			#-- Establecer localidad seleccionada inicialmente.
			if self.instance.id_localidad:
				self.initial['id_localidad'] = self.instance.id_localidad.id_localidad
		
		#-- Asegurar que exista una opción inicial en cualquier caso.
		self.fields['id_localidad'].choices.insert(0, ("", "Seleccione una localidad"))

		#-- Si es un nuevo registro.
		if not self.instance.pk:
			self.fields['id_sucursal'].initial = self.initial.get('id_sucursal')
			self.fields['id_sucursal'].widget.attrs['disabled'] = True              #-- Deshabilita el campo.
			self.fields['fecha_alta'].initial = datetime.now().strftime('%Y-%m-%d')
			self.fields['fecha_alta'].widget.attrs['readonly'] = True
			self.fields['saldo_disponible'].initial = self.fields['limite_maximo_tarjeta']
			self.fields['saldo_disponible'].widget.attrs['readonly'] = True
		else:
			self.fields['codigo_socio'].widget.attrs['readonly'] = True
			self.fields['adicional'].widget.attrs['readonly'] = True
			self.fields['digito_verificador'].widget.attrs['readonly'] = True
			self.fields['saldo_disponible'].widget.attrs['readonly'] = True
			self.fields['limite_maximo_tarjeta'].widget.attrs['readonly'] = True
			self.fields['fecha_alta'].widget.attrs['readonly'] = True
			#-- Configuración en modo edición.
			self.fields['id_sucursal'].widget = forms.HiddenInput()
			self.fields['id_sucursal'].required = False
			self.initial['id_sucursal'] = self.instance.id_sucursal
	
	def clean(self):
		cleaned_data = super().clean()
		#-- Asignar automáticamente id_sucursal si el formulario está en modo edición.
		if self.instance.pk:
			cleaned_data['id_sucursal'] = self.instance.id_sucursal
			#-- Remover id_sucursal de la validación en modo edición.
			self._errors.pop('id_sucursal', None)
		return cleaned_data
