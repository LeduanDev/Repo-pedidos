from django.db import models


class Producto(models.Model):
    nombre =  models.CharField(max_length=100, null=False)


class Categoria(models.Model):
    nombre =  models.CharField(max_length=100, null=False)



class Carrito(models.Model):
    nombre =  models.CharField(max_length=100, null=False)


class Pedidos(models.Model):
    nombre =  models.CharField(max_length=100, null=False)



# Create your models here.
