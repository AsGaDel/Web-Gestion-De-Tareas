from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from django.contrib.auth import views as auth_views
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]