from django.views.generic import ListView, TemplateView, DetailView
from registration.models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render
from tasks.models import Task

# Create your views here.

class ProfileListView(ListView):
    model = Profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Devolvemos solo los usuarios que tengan tareas en común con el usuario autenticado
        context.update({
            'profiles': Profile.objects.exclude(user=self.request.user).filter(user__tasks__in=self.request.user.tasks.all()).distinct()
        })
        return context

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.get_object().user

        # Obtener las tareas del usuario actual
        user_tasks = Task.objects.filter(members=current_user)
        
        # Obtener usuarios que comparten tareas con el usuario actual
        # Excluye al usuario actual y elimina duplicados
        related_users = User.objects.filter(
            task__in=user_tasks  # Usuarios que están en las tareas del usuario actual
        ).exclude(
            id=current_user.id  # Excluye al usuario actual
        ).distinct()  # Elimina duplicados
        
        context['users'] = related_users
        return context