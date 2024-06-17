from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, first_name = None, last_name = None, password = None):
        if not email:
            raise ValueError('El correo electrónico es requerido!')
        user = self.model (
            username = username, 
            email = self.normalize_email(email),
            first_name = first_name, 
            last_name = last_name
        )
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(
            email,
            username, 
            first_name,
            last_name
        )
        user.is_admin = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(verbose_name='Nombre de usuario', max_length=50, help_text='Ingrese el nombre de usuario...', unique=True)
    email = models.EmailField(verbose_name='Correo Electrónico', max_length=50, help_text='Ingrese el correo electrónico...', unique=True)
    first_name = models.CharField(verbose_name='Nombre', max_length=50, help_text='Ingrese su nombre...', blank=True, null=True)
    last_name = models.CharField(verbose_name='Apellido', max_length=50, help_text='Ingrese su apellido...', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)    
    
    objects = CustomUserManager()
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    def __str__(self):
        return self.username


class ProfileUser(models.Model):
    dni = models.CharField(verbose_name='Número de identificación', max_length=10, help_text='Ingrese su número de identificación', unique=True)
    avatar = models.ImageField(verbose_name='Imagen de Perfil', upload_to='avatars/', blank=True, null=True)
    birthdate = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    address = models.CharField(verbose_name='Dirección', max_length=250, help_text='Ingrese su dirección', blank=True, null=True)
    telephone = models.CharField(verbose_name='Número de teléfono', max_length=20, help_text='Ingrese su número de teléfono', blank=True, null=True)
    user = models.OneToOneField('CustomUser', on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.dni
    
    def clean(self):
        if self.dni:
            self.dni = self.dni.strip()
        if self.address:
            self.address = self.address.strip()
        if self.telephone:
            self.telephone = self.telephone.strip()