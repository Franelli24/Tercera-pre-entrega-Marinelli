# Nombre del Proyecto

Comisión: #54140

Alumno: Franco Marinelli

## Explicación breve del proyecto en cuanto al servicio
    Es un sistemas en el que se puede administrar cada comision con sus cursos, alumnos y profesores.

## Explicación breve técnica: urls, modelos, plantillas
    Urls index: sirve para volver al menu principal o ir al menu de lista.
    Urls clase_list: te lleva a la lista de comisiones.
    Urls nosotros: te lleva a una pequeña presentación sobre el creador del programa.
    Urls detalle_estudiante: te lleva a los integrantes de la comisión.
    Urls clase_create: te lleva a donde podras crear una comisión.
    Urls delete: te lleva a un menu para confirmar si queres eliminar una comisión.
    Urls clase_create_estudiante: te lleva a donde podras agregar estudiantes a una comisión.


    Modelo Curso: el curso asignado con su nombre (número).
    Modelo Estudiante: el estudiante que estará en en el curso.
    Modelo Profesor: el profesor que estará en el curso.
    Modelo Comision: agrupa todos los demas modelos para tenerlos en un mismo lugar.


    Plantilla core/index.html: guarda la imagen y el texto que aparecen en el menu principal.
    Plantilla core/base.html: guarda el diseño de lo que va a ser toda la página, junto con su encabezado y pie en  una carpeta aparte llamada 'components'.
    Plantilla clase/nosotros.hmtl: guarda el mensaje del creador para los visitantes.
    Plantilla clase/index.hmtl: guarda los links para ir a ver la lista de comisiones y para crear una.
    Plantilla clase/list.html: guarda un buscador de comisiones que se buscan por nombre de curso y profesor, y muestra las comisiones con los botones para borrar y ver estudiantes.
    Plantilla clase/detalle_estudiante.html: guarda una lista con los estudiantes que pertenecen a dicha comisión y un botón para agregar estudiantes.
    Plantilla clase/clase_estudiante_form.html: guarda el formulario (guardado en el archivo forms.py) para llenar el nombre del estudiante que quiere agregar junto con el botón de guardar.
    Plantilla clase/clase_confirm_delete.html: guarda un botón con una pregunta para confirmar si quiere borrar la comisión elegida.
    Plantilla clase/clase_form.html: guarda el formulario (guardado en el archivo forms.py) para crear una comisión llenar los datos de nombre de comisión, curso y profesor.

## Mejoras futuras
    Poder agregar estudiantes a sus respectivas comisiones sin tener que ir a editar la comisión.

## Problemas conocidos
    No se agregan los estudiantes a la lista automáticamente.