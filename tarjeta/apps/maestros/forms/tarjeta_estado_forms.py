# tarjeta\apps\maestros\forms\tarjeta_estado_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import TarjetaEstado
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect)


class TarjetaEstadoForm(CrudGenericForm):
	
	class Meta:
		model = TarjetaEstado
		fields = '__all__'

		widgets = {
			'estatus_tarjeta_estado': 
				forms.Select(attrs={**formclassselect}), 
			'descripcion_tarjeta_estado': 
				forms.TextInput(attrs={**formclasstext}),
			'mensaje': 
				forms.TextInput(attrs={**formclasstext}),
		}
