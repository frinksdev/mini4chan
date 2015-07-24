from django import forms
from .models import chan, comentario

class post(forms.ModelForm):
	class Meta:
		model=chan
		fields=("titulo","contenido",)

class comentar(forms.ModelForm):
	class Meta:
		model=comentario
		fields=("comentario",)