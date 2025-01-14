from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    U_ID = models.IntegerField(db_column='U_ID', null=True)
    username = models.CharField(db_column='U_Username', max_length=45, unique=True)
    U_fullname = models.CharField(db_column='U_FullName', max_length=45, null=True , blank=True)
    U_sex = models.CharField(db_column='U_Sex', max_length=45, null=True, blank=True)
    U_address = models.CharField(db_column='U_Address', max_length=255, null=True, blank=True)
    U_Role = models.CharField(db_column='U_Role', max_length=45, null=True, blank=True)
    U_phone = models.CharField(db_column='U_Phone', max_length=45, null=True, blank=True)
    RG_ID = models.CharField( db_column='RG_ID', max_length=45, null=True, blank=True)
    is_staff = models.BooleanField(db_column='is_staff', default=True)
    is_employee = models.BooleanField(db_column='is_manager', default=False)
    is_admin = models.BooleanField(db_column='is_admin', default=False)
    is_superuser = models.BooleanField(db_column='is_superuser', default=False)
    is_active = models.BooleanField(db_column='is_active', default=True)
    date_joined = models.DateTimeField(db_column='date_joined', default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
    
    