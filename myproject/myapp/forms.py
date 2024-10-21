from django import forms
from .models import cake_order
class cake_order_form(forms.ModelForm):
	class Meta:
		model=cake_order
		fields="__all__"
