from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from tasks.models import Task

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'core/home.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'pending_tasks_count': Task.objects.filter(state='pendiente').count(),
            'in_progress_tasks_count': Task.objects.filter(state='en_proceso').count(),
            'completed_tasks_count': Task.objects.filter(state='completada').count(),
            'recent_tasks': Task.objects.all().order_by('-created_date')[:5]
        })
        return context


class AboutPageView(TemplateView):
    template_name = 'core/about.html'

