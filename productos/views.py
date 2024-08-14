
from django.shortcuts import render
from productos.models import Producto, Categoria


def inicio(request):
    producto = Producto.objects.all()
    context = {
        'producto': producto
    }
    return render (request, 'paginas/index.html', context)


