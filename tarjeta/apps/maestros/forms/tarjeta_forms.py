# tarjeta\apps\maestros\forms\tarjeta_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import *
from ..models.tarjeta_models import Tarjeta
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
				forms.NumberInput(attrs={**formclasstext, 
							'readonly': True}),
			'numero_tarjeta':  
				forms.NumberInput(attrs={**formclasstext, 
							'readonly': True}), 
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
				forms.NumberInput(attrs={**formclasstext, 'readonly': True, 
                           'min': 0, 'max': 999999999, 'step': '0.01'}),
			'saldo_disponible': 
				forms.NumberInput(attrs={**formclasstext, 'readonly': True,
                           'min': 0, 'max': 999999999, 'step': '0.01'}),
			'id_titulo': 
				forms.Select(attrs={**formclassselect}), 
			'id_tarjeta_estado': 
				forms.Select(attrs={**formclassselect}), 
			'fecha_alta': 
				forms.TextInput(attrs={'type':'date', **formclassdate, 'readonly': True}),
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
		super().__init__(*args, **kwargs)
		# Verifica si estamos editando un registro con provincia ya seleccionada
		if self.instance and self.instance.pk and self.instance.id_provincia:
			# self.fields['id_localidad'].queryset = Localidad.objects.filter(id_provincia=self.instance.id_provincia).order_by('nombre_localidad')
   
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
		self.fields['id_localidad'].empty_label = "Seleccione una localidad"
		
		###################################################################################
		#-- Si es un nuevo registro.
		if not self.instance.pk:
			self.fields['id_sucursal'].initial = self.initial.get('id_sucursal')
			#-- Deshabilita el campo.
			self.fields['id_sucursal'].widget.attrs['disabled'] = True
		else:
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
	
