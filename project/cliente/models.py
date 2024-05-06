from django.db import models

# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.nombre
    class meta():
        verbose_name = "País"
        verbose_name_plural = "Países"

class Provincia(models.Model):
    nombre = models.CharField(Pais,max_length=50, unique=True)
    def __str__(self) -> str:
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=80, null=False)
    apellido = models.CharField(max_length=80, null=False)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, on_delete= models.SET_NULL,null=True, blank=True, verbose_name="País de Origen")
    provincia = models.ForeignKey(Provincia, on_delete= models.SET_NULL, null=True, blank=True)
    def __str__(self) -> str:
        return (f"{self.apellido} {self.nombre}")