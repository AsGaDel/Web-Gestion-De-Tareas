from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from .forms import TaskForm
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Task

# Create your views here.

# Mixin para requerir roles de usuario antes de realizar una acción
class RolesRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.groups.filter(name__in=['Personal', 'Administradores']).exists():
            return redirect(reverse_lazy('login'))
        return super(RolesRequiredMixin, self).dispatch(request, *args, **kwargs)

class TasksView(TemplateView):
    template_name = 'tasks/tasks.html'
    
    # Sobreescribimos el método get_context_data para enviar datos adicionales al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Si el usuario no está autenticado, no se envían tareas
        if not self.request.user.is_authenticated:
            return context
        # Filtramos las tareas que pertenecen al usuario autenticado
        context.update({
            'tasks': Task.objects.filter(members=self.request.user).select_related('category').prefetch_related('members')
        })
        return context
    
# Vista basada en clase para crear una tarea. Se requiere que el usuario esté autenticado y pertenezca a los grupos 'Personal' o 'Administradores'
class TaskCreateView(RolesRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        # Establece la fecha de creación automáticamente
        form.instance.created_date = timezone.now()
        return super().form_valid(form)
    

class TaskDeleteView(RolesRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.groups.filter(name__in=['Personal', 'Administradores']).exists():
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)

class TaskUpdateView(RolesRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.modified_date = timezone.now()
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.groups.filter(name__in=['Personal', 'Administradores']).exists():
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)
    

