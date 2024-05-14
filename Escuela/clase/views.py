from django.shortcuts import render, get_object_or_404, redirect

from clase.models import Comision
from clase.forms import ClaseListForm

def index(request):
    return render(request, "clase/index.html")

def clase_list(request):
    consulta = Comision.objects.all()
    contexto = {"comisiones": consulta}
    return render(request, "clase/clase_list.html", contexto)

def nosotros(request):
    return render(request, "clase/nosotros.html")

def detalle_estudiante(request, comision_id):
    comision = get_object_or_404(Comision, pk=comision_id)
    estudiantes = comision.estudiante.all()
    return render(request, 'clase/detalle_estudiante.html', {'comision': comision, 'estudiantes': estudiantes})

def clase_create(request):
    if request.method == "POST":
        form = ClaseListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clase:clase_list")
    else:  # GET
        form = ClaseListForm()
    return render(request, "clase/clase_form.html", {"form": form})