from django.urls import path

from clase.views import clase_list, index, nosotros, detalle_estudiante

app_name = "clase"

urlpatterns = [
    path("", index, name="index"),
    path("clase/clase_list",clase_list, name="clase_list"),
    path("clase/nosotros",nosotros, name="nosotros"),
    path('clase/detalle_estudiante/<int:comision_id>',detalle_estudiante, name='detalle_estudiante'),
]