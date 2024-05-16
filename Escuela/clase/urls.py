from django.urls import path

from clase.views import (
    index, 
    nosotros,
    detalle_estudiante, 
    clase_create_estudiante
)
from clase.views import ClaseList, ClaseCreate, ClaseUpdate, ClaseDelete

app_name = "clase"

urlpatterns = [
    path("", index, name="index"),
    path("clase/nosotros",nosotros, name="nosotros"),
    path('clase/detalle_estudiante/<int:comision_id>',detalle_estudiante, name='detalle_estudiante'),
    path("clase/clase_create_estudiante/<int:comision_id>", clase_create_estudiante, name="clase_create_estudiante"),
]

urlpatterns += [
    path("clase/clase_list", ClaseList.as_view(), name="clase_list"),
    path("clase/clase_create", ClaseCreate.as_view() , name="clase_create"),
    path("clase/update/<int:pk>", ClaseUpdate.as_view(), name="clase_update"),
    path("clase/delete/<int:pk>", ClaseDelete.as_view() , name="clase_delete"),
]