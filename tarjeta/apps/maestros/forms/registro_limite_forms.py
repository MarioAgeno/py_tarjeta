# tarjeta\apps\maestros\forms\registro_limite_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.tarjeta_models import RegitroLimite
from diseno_base.diseno_bootstrap import (formclassdate,
	formclasstext, formclassselect)


class RegitroLimiteForm(CrudGenericForm):
	
	class Meta:
		model = RegitroLimite
		fields = '__all__'

		widgets = {
			'estatus_registro_limite': 
				forms.Select(attrs={**formclassselect}), 
			'id_tarjeta': 
				forms.Select(attrs={**formclassselect}), 
			'fecha_limite': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'maximo_limite': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999999999, 'step': '1.00'}),
		}
