# tarjeta\apps\maestros\forms\tarjeta_forms.py
import requests
from django.core.exceptions import ValidationError
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import *
from ..models.tarjeta_models import Tarjeta
from datetime import datetime
from diseno_base.diseno_bootstrap import (formclassdate,
	formclasstext, formclassselect, formclasscheck)

import logging

# Configuración básica del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Puedes cambiar a DEBUG si deseas más información
ch = logging.StreamHandler()  # Para mostrar los logs en la consola
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


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
			self.fields['id_localidad'].choices = []
			
		# Opcional: si quieres que se muestre un mensaje de "Seleccione una localidad"
		self.fields['id_localidad'].empty_label = "Seleccione una localidad"
		
		#-- Si es un nuevo registro.
		if not self.instance.pk:
			self.fields['id_sucursal'].initial = self.initial.get('id_sucursal')
			self.fields['fecha_alta'].initial = datetime.now().strftime('%Y-%m-%d')
			self.fields['fecha_alta'].widget.attrs['readonly'] = True
			self.fields['saldo_disponible'].initial = self.fields['limite_maximo_tarjeta']
			self.fields['saldo_disponible'].widget.attrs['readonly'] = True
		else:
			self.fields['id_sucursal'].widget.attrs['disabled'] = True
			self.fields['codigo_socio'].widget.attrs['readonly'] = True
			self.fields['adicional'].widget.attrs['readonly'] = True
			self.fields['digito_verificador'].widget.attrs['readonly'] = True
			self.fields['saldo_disponible'].widget.attrs['readonly'] = True
			self.fields['limite_maximo_tarjeta'].widget.attrs['readonly'] = True
			self.fields['fecha_alta'].widget.attrs['readonly'] = True

	def clean_codigo_socio(self):
		codigo_socio = self.cleaned_data.get('codigo_socio')
		if codigo_socio:
			try:
				logger.info(f'Consultando API para el código de socio: {codigo_socio}')
				response = requests.get(f'http://127.0.0.1:5000/sociocodigo/{codigo_socio}')
					
				if response.status_code == 200:
					socio_data = response.json()
					logger.info(f'Datos obtenidos para el socio: {socio_data}')
					
					# Asigna los valores a los campos directamente
					self.fields['nombre_titular'].initial = socio_data.get('Nombre')
					self.fields['domicilio'].initial = socio_data.get('Domicilio')
					self.fields['telefono_tarjeta'].initial = socio_data.get('Telefono')
					self.fields['telefono2_tarjeta'].initial = socio_data.get('Telefono 2')
					self.fields['movil_tarjeta'].initial = socio_data.get('Movil')
					self.fields['mail_tarjeta'].initial = socio_data.get('e-Mail')
				else:
					logger.error(f'No se encontró el socio con el código {codigo_socio}, API respondió con status {response.status_code}')
					raise ValidationError("No se encontró el socio con el código ingresado.")
			except Exception as e:
				logger.error(f"Error al obtener los datos del socio: {e}")
				raise ValidationError(f"Error al obtener los datos del socio: {e}")
		return codigo_socio


'''
	def clean_codigo_socio(self):
		codigo_socio = self.cleaned_data.get('codigo_socio')
		if codigo_socio:
			try:
				logger.info(f'Consultando API para el código de socio: {codigo_socio}')
				response = requests.get(f'http://127.0.0.1:5000/sociocodigo/{codigo_socio}')
				
				if response.status_code == 200:
					socio_data = response.json()
					logger.info(f'Datos obtenidos para el socio: {socio_data}')
					
					# Asigna los valores a cleaned_data para que se puedan reflejar en el formulario
					self.cleaned_data['nombre_titular'] = socio_data.get('Nombre')
					self.cleaned_data['domicilio'] = socio_data.get('Domicilio')
					self.cleaned_data['telefono_tarjeta'] = socio_data.get('Telefono')
					self.cleaned_data['telefono2_tarjeta'] = socio_data.get('Telefono 2')
					self.cleaned_data['movil_tarjeta'] = socio_data.get('Movil')
					self.cleaned_data['mail_tarjeta'] = socio_data.get('e-Mail')
					
					# También puedes establecer valores en initial si los valores deben ser persistentes
					self.initial['nombre_titular'] = socio_data.get('Nombre')
					self.initial['domicilio'] = socio_data.get('Domicilio')
					self.initial['telefono_tarjeta'] = socio_data.get('Telefono')
					self.initial['telefono2_tarjeta'] = socio_data.get('Telefono 2')
					self.initial['movil_tarjeta'] = socio_data.get('Movil')
					self.initial['mail_tarjeta'] = socio_data.get('e-Mail')
				else:
					logger.error(f'No se encontró el socio con el código {codigo_socio}, API respondió con status {response.status_code}')
					raise ValidationError("No se encontró el socio con el código ingresado.")
			except Exception as e:
				logger.error(f"Error al obtener los datos del socio: {e}")
				raise ValidationError(f"Error al obtener los datos del socio: {e}")
		return codigo_socio
'''


