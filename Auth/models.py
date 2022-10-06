from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class CreateUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(
            email = self.normalize_email(email), 
            username = username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email= email, 
            username= username, 
            password = password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        
        return user     

class User(AbstractBaseUser, PermissionsMixin):
    
    username=models.CharField(max_length=255,null=True,blank=True,unique=True)
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=255,unique=True)
    business_name = models.CharField(max_length=255,null=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = CreateUserManager()
    
    def __str__(self):
        return self.username
    
