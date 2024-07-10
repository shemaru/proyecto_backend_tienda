from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, password, last_name, is_staff, is_superuser, **args):
        user = self.model(
            username = username,
            email = email,
            name = name,
            password = password,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **args      
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_user(self, username, email, name, password, last_name, **args):
        return self._create_user(username, email, name, password, last_name, False, False, **args)
    
    def create_superuser(self, username, email, name, password, last_name, **args):
        return self._create_user(username, email, name, password, last_name, True, True, **args)
        

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Usuario', max_length = 255, unique = True)
    email = models.EmailField('Email', max_length = 255, unique = True)
    name = models.CharField('Nombres', max_length = 255)
    last_name = models.CharField('Apellidos', max_length = 255)
    image = models.ImageField('Imagen de perfil', upload_to ='perfil/',max_length = 255, null = False, blank = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']
