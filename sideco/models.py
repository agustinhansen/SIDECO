from django.db import models

# Create your models here.

class Sistema(models.Model):
    def lista_empresa():
    def lista_desempleado():
    def dar_de_alta_desempleado():
    def dar_de_alta_empresa():
    def enviar_informacion_desempleado():
    def listado_desempleado():
    def almacenamiento_historico():
    
class Persona(models.Model): 
    DNI = models.CharField(max_length=10)
    tipo_de_trabajo = models.TextField()
    fecha_de_nacimiento = models.TextField()
    
class Empleado(models.Model):
    empresa = models.ForeignKey('Empresa')

class Desempleado(models.Model):
  
class Empresa(models.Model):
    CUIL = models.CharField(max_length=12)
    razon_social = models.TextField()
    rubro = models.TextField()
    
    def contratar_desempleado():
      
class OfertaLaboral(models.Model):
    empresa = models.ForeignKey('Empresa')
    tipo_de_trabajo_solicitado = models.TextField()
