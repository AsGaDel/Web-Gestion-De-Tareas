from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Escribe tu nombre', 'class': 'form-input',
            'id': 'name', 'name': 'name'}
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Escribe tu email', 'class': 'form-input', 'id': 'email', 'name': 'email'}
    ))
    subject = forms.CharField(label='Asunto', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Escribe el asunto', 'class': 'form-input', 'id': 'subject', 'name': 'subject'}
    ))
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={'rows': 3, 'placeholder': 'Escribe tu mensaje', 'class': 'form-textarea', 'id': 'message', 'name': 'message'}
    ))