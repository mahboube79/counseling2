from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email,name,family,mobile_number,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not mobile_number:
            raise ValueError('Users must have a mobile number')
        
        user= self.model(
            email= self.normalize_email(email),
            name=name,
            family=family,
            mobile_number=mobile_number
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,family,mobile_number,password=None):
        user= self.create_user(
             email,
             password=password,
             name=name ,
             family=family,
             mobile_number=mobile_number,
        )
        user.is_active=True
        user.is_admin=True
        user.save(using=self._db)
        return user
     
     
# -----------------------------------------------------------------
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=200,unique=True)
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=11,unique=True)
    gender = models.BooleanField(default=True,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_admin= models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','family','mobile_number']
    
    objects=CustomUserManager()
    def __str__(self):
        return self.email
    
    def has_perm(self,perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    