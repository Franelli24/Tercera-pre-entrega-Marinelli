from django.shortcuts import render

from . import models

def index(request):
    consulta = models.Comision.objects.all()
    contexto = {"comisiones": consulta}
    return render(request, "clase/index.html", contexto)