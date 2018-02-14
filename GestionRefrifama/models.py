from django.db import models

class Persona(models.Model):
	codigo = models.CharField(max_length=10, primary_key=True, help_text='Escribe cedula')
	primer_nombre = models.CharField(max_length=30)
	segundo_nombre = models.CharField(blank=True, max_length=30)
	telefono = models.CharField(max_length=30)


    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
    

class Producto(models.Model):

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        pass
    
