from django.db import models

# Create your models here.
class Curso (models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField ()
    
    def __str__(self): 
        return self.nombre
    
class Estudiante (models.Model):
    nombre   = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email    = models.EmailField(null=True)
    
    
class Profesor (models.Model):
    nombre   = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email    = models.EmailField(null=True)    
    profesion = models.CharField(max_length=50) 
    cursos = models.ManyToManyField(Curso)
    
    def __str__(self): 
        return f'{self.nombre} {self.apellido}'
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega =models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiante, on_delete =models.CASCADE)