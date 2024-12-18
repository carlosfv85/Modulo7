from django.forms import ModelForm
from django import forms
from .models import Laboratorio



class LaboratorioFormCreate(ModelForm):
    class Meta:
        model = Laboratorio
        fields = [
            'nombre', 
            'ciudad',
            'pais',
        ]
        
        labels = {
            "Pais": ("País"),  
        }
         
        widgets = {
            "nombre": forms.TextInput(attrs={"class": 'form-control'}),
            "ciudad": forms.TextInput(attrs={"class": 'form-control'}),
            "pais": forms.TextInput(attrs={"class": 'form-control'}),
        }

