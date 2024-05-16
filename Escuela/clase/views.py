from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from clase.models import Comision
from clase.forms import ClaseListForm, ClaseEstudianteForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView,DeleteView

def index(request):
    return render(request, "clase/index.html")

# def clase_list(request):
#     busqueda = request.GET.get("busqueda", None)
#     if busqueda:
#         consulta = Comision.objects.filter(curso__nombre__icontains=busqueda)
#     else:
#         consulta = Comision.objects.all()
#     contexto = {"comisiones": consulta}
#     return render(request, "clase/clase_list.html", contexto)

class ClaseList(ListView):
    model = Comision
    template_name = "clase/clase_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Comision.objects.filter(
                Q(curso__nombre__icontains=busqueda) | Q(profesor__nombre__icontains=busqueda)
                )
        return queryset

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

def clase_create_estudiante(request, comision_id):
    if request.method == "POST":
        form = ClaseEstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la vista detalle_estudiante con el comision_id dado
            return HttpResponseRedirect(reverse('clase:detalle_estudiante', args=[comision_id]))
    else:  # GET
        form = ClaseEstudianteForm()
    return render(request, "clase/clase_estudiante_form.html", {"form": form})

def clase_delete(request, pk: int):
    consulta = Comision.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("clase:clase_list")
    return render(request, "clase/clase_confirm_delete.html", {"object": consulta})