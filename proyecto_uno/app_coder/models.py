from django.db import models
from django.contrib.auth.models import User



class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    nacimiento = models.DateField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    nacimiento = models.DateField()


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True) 