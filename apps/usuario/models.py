from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, first_name, last_name, password, is_admin, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es requerido!')
        user = self.model (
            username = username, 
            email = self.normalize_email(email),
            first_name = first_name, 
            last_name = last_name,
            is_admin = is_admin,
            is_superuser = is_superuser,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, first_name=None, last_name=None, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, first_name=None, last_name=None, password = None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Nombre de usuario', max_length=50, unique=True)
    email = models.EmailField(verbose_name='Correo Electrónico', max_length=50, unique=True)
    first_name = models.CharField(verbose_name='Nombre', max_length=50, blank=True, null=True)
    last_name = models.CharField(verbose_name='Apellido', max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)    
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin



class ProfileUser(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    dni = models.CharField(verbose_name='Número de identificación', max_length=10, help_text='Ingrese su número de identificación', unique=True, blank=True, null=True)
    avatar = models.ImageField(verbose_name='Imagen de Perfil', upload_to='avatars/', blank=True, null=True)
    birthdate = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    address = models.CharField(verbose_name='Dirección', max_length=250, help_text='Ingrese su dirección', blank=True, null=True)
    telephone = models.CharField(verbose_name='Número de teléfono', max_length=20, help_text='Ingrese su número de teléfono', blank=True, null=True)
    
    def __str__(self):
        return self.user.username if self.user.username else "usuario vacio"
    
    def clean(self):
        if self.dni:
            self.dni = self.dni.strip()
        if self.address:
            self.address = self.address.strip()
        if self.telephone:
            self.telephone = self.telephone.strip()