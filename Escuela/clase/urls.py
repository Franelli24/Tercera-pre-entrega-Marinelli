from django.urls import path

from clase.views import( 
    clase_list, 
    index, 
    nosotros, 
    detalle_estudiante, 
    clase_create,  
    clase_delete
)

app_name = "clase"

urlpatterns = [
    path("", index, name="index"),
    path("clase/clase_list",clase_list, name="clase_list"),
    path("clase/nosotros",nosotros, name="nosotros"),
    path('clase/detalle_estudiante/<int:comision_id>',detalle_estudiante, name='detalle_estudiante'),
    path("clase/clase_create", clase_create, name="clase_create"),
    path("clase/delete/<int:pk>", clase_delete, name="clase_delete"),
]