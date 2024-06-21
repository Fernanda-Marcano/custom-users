from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ProfileUser

class CustomUserForm(UserCreationForm):    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = '__all__'
        """ widgets = {
            'birthdate':forms.DateField(format=('%Y-%m-%d'), type='date')
        } """
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