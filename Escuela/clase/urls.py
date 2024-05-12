from django.urls import path

from clase.views import clase_list, index, nosotros

app_name = "clase"

urlpatterns = [
    path("", index, name="index"),
    path("clase/clase_list",clase_list, name="clase_list"),
    path("clase/nosotros",nosotros, name="nosotros")
]