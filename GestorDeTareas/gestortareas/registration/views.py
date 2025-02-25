from .forms import UserCreationFormWithEmail, ProfileUpdateForm, EmailForm, VerificationCodeForm
from django.views.generic import CreateView, UpdateView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(TemplateView):
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        context['profile'] = profile
        return context

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
    def form_valid(self, form):
        # Primero manejamos la eliminación de la imagen si es necesario
        if form.cleaned_data.get('delete_picture'):
            form.instance.picture = "registration/img/no-avatar.jpg"
        # Luego llamamos al form_valid del padre y retornamos su resultado
        return super().form_valid(form)
    
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('verification_code')
    template_name = 'registration/email_form.html'

    def get_object(self):
        return self.request.user
    
    def get_form(self, form_class = ...):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].initial = self.request.user.email
        return form

    def form_valid(self, form):
        self.object.email = form.cleaned_data.get('email')
        self.object.save()
        return super().form_valid(form)
    
class VerificationCodeView(TemplateView):
    template_name = 'registration/verification_code.html'
    success_url = reverse_lazy('email_update')
