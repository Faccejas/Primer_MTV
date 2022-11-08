from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from app_MTV.models import Familia

def vista_plantilla(request):

    listado_familiares = Familia.objects.all()

    datos = {"listado familiares": listado_familiares}

    plantilla = loader.get_template("plantilla_datos.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)