from django.db import models


class Producto(models.model):
    nombre =  models.CharField(max_length=100, null=False)


class Categoria(models.model):
    nombre =  models.CharField(max_length=100, null=False)



class Carrito(models.model):
    nombre =  models.CharField(max_length=100, null=False)


class Pedidos(models.model):
    nombre =  models.CharField(max_length=100, null=False)



# Create your models here.
