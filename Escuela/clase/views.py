from django.shortcuts import render

from clase.models import Comision

def index(request):
    return render(request, "clase/index.html")

def clase_list(request):
    consulta = Comision.objects.all()
    contexto = {"clases": consulta}
    return render(request, "clase/clase_list.html", contexto)