# tarjeta\apps\maestros\forms\actividad_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import Actividad
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect)


class ActividadForm(CrudGenericForm):
	
	class Meta:
		model = Actividad
		fields = '__all__'

		widgets = {
			'estatus_actividad': 
				forms.Select(attrs={**formclassselect}), 
			'nombre_actividad': 
				forms.TextInput(attrs={**formclasstext}),
			'interes_actividad': 
				forms.NumberInput(attrs={**formclasstext,
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'codigo_afip': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999}),
		}
