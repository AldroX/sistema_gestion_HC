from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict

class Paciente(models.Model):
    nombrePaciente= models.CharField(max_length=150,verbose_name='Nombre Paciente'  )
    apellidoPaciente= models.CharField(max_length=150)
    CI= models.CharField(max_length=12)
    fechaNaciemiento= models.DateField(null=True)
    direccionPaciente = models.TextField(blank=False)
    numeroTelefonico = models.CharField(max_length=11)
    estado = models.BooleanField(default=True,verbose_name='Estado')


    def __str__(self):
        return self.nombrePaciente

    def toJSON(self):
        item  = model_to_dict(self)
        return item
    


