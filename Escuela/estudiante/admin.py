from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Estudiante"

class ClaseAdmin(admin.ModelAdmin):
    list_display = (
        "estudiante",
        "comision",
        "fecha_inscripcion",
    )
    list_display_links = ("comision",)
    search_fields = ("comision.curso", "estudiante")
    list_filter = ("estudiante",)
    date_hierarchy = "fecha_inscripcion"


admin.site.register(models.Estudiante)
admin.site.register(models.Clase, ClaseAdmin)