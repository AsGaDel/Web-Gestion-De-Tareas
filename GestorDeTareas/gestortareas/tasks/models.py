from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    deadline = models.DateTimeField(verbose_name='Fecha límite')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Categoría', null=True, blank=True)
    members = models.ManyToManyField('auth.User', verbose_name='Miembros')
    state_options = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('completada', 'Completada')
    ]
    
    state = models.CharField(
        max_length=20,
        choices=state_options,
        default='pendiente', verbose_name='Estado'
    )

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.name