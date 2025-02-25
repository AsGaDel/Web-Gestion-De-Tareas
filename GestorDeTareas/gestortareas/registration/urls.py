from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import SignUpView, ProfileUpdateView, ProfileView, EmailUpdate, VerificationCodeView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email'),
    path('profile/email/verification_code/', VerificationCodeView.as_view(), name='verification_code')
]