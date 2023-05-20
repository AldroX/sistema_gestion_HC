from typing import Any
from django.forms import *
from .models import Paciente

class PacienteForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for form in self.visible_fields():
    #         form.field.widget.attrs.update({"class": "form-control"})
          
    class Meta:
        model =Paciente
        fields = ['nombrePaciente','apellidoPaciente','CI','fechaNaciemiento',
                  'direccionPaciente','numeroTelefonico']
        labels = {
             
             'nombrePaciente': 'Nombre del Paciente' ,
             'apellidoPaciente': 'Apellido del Paciente'  ,
             'CI': 'Carnet de Identidad',
             'fechaNaciemiento': 'Fecha de Nacimiento' ,
             'direccionPaciente': 'Direccion del Paciente ', 
             'numeroTelefonico': 'Numero Telefonico' , 
        }

        widgets = {
            'nombrePaciente': TextInput( attrs = {
             'placeholder': 'Introducir  nombre',
             'class': 'form-control',
             } ),

             'apellidoPaciente': TextInput(attrs={
             'placeholder': 'Introducir Apellido',
             'class': 'form-control',
             }),
            
               'CI': TextInput(attrs={
             'placeholder': 'Introducir carnet de identidad',
             'class': 'form-control',

             }),

                'fechaNaciemiento': DateInput(attrs={
             'placeholder': 'Introducir fecha de nacimiento',
             'class': 'form-control',
             }),

                 'direccionPaciente': Textarea(attrs={
             'placeholder': 'Introducir direccion particular',
             'class': 'form-control',
             }),

                  'numeroTelefonico': TextInput(attrs={
             'placeholder': 'Introducir numero telefonico',
             'class': 'form-control',
             }),

 
         }
        

 

        