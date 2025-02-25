from django.contrib import admin

# Register your models here.

from .models import Task, Category

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date') # Para que no se puedan editar las fechas de creación y actualización
    list_display = ('title', 'category', 'state', 'deadline', 'task_users' ) # Para mostrar título, categoría, estado y fecha límite
    ordering = ('state', 'deadline') # Para ordenar por estado y fecha límite
    search_fields = ('title', 'category__name') # Para buscar por título y categoría
    date_hierarchy = 'deadline' # Para filtrar por fecha
    list_filter = ('state', 'category__name') # Para filtrar por estado y categoría

    def task_users(self, obj): 
        return ", ".join([user.username for user in obj.members.all()]) # Para mostrar los usuarios de la tarea como una cadena separada por comas
    task_users.short_description = "Usuarios"

admin.site.register(Task, TaskAdmin) # Para registrar la clase TaskAdmin
admin.site.register(Category) # Para registrar la clase Category
