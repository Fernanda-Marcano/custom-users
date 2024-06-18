from django import forms
from .models import CustomUser, ProfileUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'help_text':'Ingrese su contraseña'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'help_text':'Ingrese nuevamente su contraseña'
    }))
    
    class Meta:
        model = CustomUser
        exclude = ['is_active', 'is_admin']
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if confirm_password != password:
            raise ValueError('Las contraseñas no coinciden. Las contraseñas deben ser iguales')
        return confirm_password


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        exclude = 'user'
        widgets = {
            'birthdate':forms.DateField(format=('%Y-%m-%d'), type='date')
        }
        labels = {
            'dni':'DNI',
            'avatar':'Avatar', 
            'birthdate':'Fecha de Nacimiento', 
            'address':'Dirección', 
            'telephone':'Número de Teléfono'
        }
    
    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if dni < 10 and dni != dni.isdecimal():
            raise ValueError('El número de identificación no es válido')
        return dni