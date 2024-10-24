# neumatic\apps\maestros\forms\actividad_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import Plan
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect, formclassdate)


class PlanForm(CrudGenericForm):
	
	class Meta:
		model = Plan
		fields = '__all__'

		widgets = {
			'estatus_plan': 
				forms.Select(attrs={**formclassselect}), 
			'nombre_plan': 
				forms.TextInput(attrs={**formclasstext}),
			'cuotas_plan': 
				forms.NumberInput(attrs={**formclasstext,
                           'min': 1, 'max': 99, 'step': '1'}),
			'interes_plan': 
				forms.NumberInput(attrs={**formclasstext,
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'costo_financiero_plan': 
				forms.NumberInput(attrs={**formclasstext,
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'vencimiento_plan': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
		}
