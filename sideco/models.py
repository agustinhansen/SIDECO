from django.db import models

# Create your models here.

class Sistema(models.Model):
    def lista_empresa():
        pass     
    def lista_desempleado():
        pass
    def dar_de_alta_desempleado():
        pass
    def dar_de_alta_empresa():
        pass
    def enviar_informacion_desempleado():
        pass
    def listado_desempleado(): 
        pass
    def almacenamiento_historico():
        pass
    
class Persona(models.Model): 
    DNI = models.CharField(max_length=10)
    tipo_de_trabajo = models.TextField()
    fecha_de_nacimiento = models.TextField()
    
class Empleado(Persona):
    empresa = models.ForeignKey('Empresa')

class Desempleado(Persona):
    pass

class Empresa(models.Model):
    cuil = models.CharField(max_length=12)
    razon_social = models.TextField()
    rubro = models.TextField() 

    def contratar_desempleado():
       pass

class OfertaLaboral(models.Model):
    empresa = models.ForeignKey('Empresa')
    tipo_de_trabajo_solicitado = models.TextField()
