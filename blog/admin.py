from django.contrib import admin

from .models import Usuario, Tarea, Etiqueta, AsignacionTarea, Comentario, Proyecto

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(Etiqueta)
admin.site.register(AsignacionTarea)
admin.site.register(Comentario)
admin.site.register(Proyecto)
