from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100, verbose_name='Marca', null=True)
    modelo = models.CharField(max_length=100, verbose_name='Modelo', null=True)
    placa = models.CharField(max_length=100, verbose_name='Placa', null=True)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)

def __str__(self):
    fila = self.marca + self.modelo  + self.placa
    return fila

def delete(self, using=None, keep_parents=False):
    self.imagen.storage.delete(self.imagen.name)
    super().delete()
