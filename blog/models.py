from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=128)
    fecha_registro = models.DateTimeField()

    def __str__(self):
        return self.correo_electronico

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField(null=True, blank=True)
    colaboradores = models.ManyToManyField(Usuario, related_name='proyectos_asignados')
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTAD_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completada', 'Completada'),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTAD_CHOICES, default='Pendiente')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='tareas_etiquetadas', blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas_proyecto')
    asignados = models.ManyToManyField(Usuario, through='AsignacionTarea', blank=True)

    def __str__(self):
        return self.titulo

class AsignacionTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    observaciones = models.TextField(null=True, blank=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tarea} - {self.usuario}'
    

class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} - {self.tarea}'