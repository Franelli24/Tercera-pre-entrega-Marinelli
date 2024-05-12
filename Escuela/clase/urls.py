from django.urls import path

from clase.views import clase_list, index

app_name = "clase"

urlpatterns = [
    path("", index, name="index"),
    path("clase/list",clase_list, name="clase_list"),
]