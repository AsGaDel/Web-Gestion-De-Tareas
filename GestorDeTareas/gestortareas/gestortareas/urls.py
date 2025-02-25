"""
URL configuration for gestortareas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import TasksView
from tasks.views import TaskCreateView, TaskDeleteView, TaskUpdateView
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('contact/', include('contact.urls')),
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    # Paths de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
