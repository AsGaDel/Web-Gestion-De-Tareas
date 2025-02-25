from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 caracteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar los widgets
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirmar contraseña'
        })

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email

class ProfileUpdateForm(forms.ModelForm):
    delete_picture = forms.BooleanField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = Profile
        fields = ['picture', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Cuéntanos sobre ti...',
                'rows': 4
            }),
            'picture': forms.FileInput(attrs={
                'class': 'hidden-input',
                'accept': 'image/*'
            })
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 caracteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email'
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data and User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email
    
class VerificationCodeForm(forms.Form):
    code = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Código de verificación'
    }))

    class Meta:
        fields = ['code']
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Código de verificación'
            })
        }
    
