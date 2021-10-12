
from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"
                
    def __str__ (self):
        return self.nombre


class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    stock=models.BigIntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
        
    def __str__(self):
        return self.nombre
    