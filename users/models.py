from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    User_sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    User_Role = (
        ('ReferralPhysician', 'Referral Physician'),
        ('Radiologist', 'Radiologist'),
        ('Admin', 'Admin'),
        ('SuperAdmin', 'Super Admin'),
    )


    U_ID = models.IntegerField(db_column='U_ID', null=True , verbose_name='User_ID')
    username = models.CharField(db_column='U_Username', max_length=45, unique=True)
    U_fullname = models.CharField(db_column='U_FullName', max_length=45, null=True , blank=True, verbose_name='Full Name')
    U_sex = models.CharField(db_column='U_Sex', max_length=45, null=True, blank=True, choices=User_sex , verbose_name='Gender')
    U_address = models.CharField(db_column='U_Address', max_length=255, null=True, blank=True, verbose_name='Address')
    U_Role = models.CharField(db_column='U_Role', max_length=45, null=True, blank=True, choices=User_Role , verbose_name='User Role')
    U_phone = models.CharField(db_column='U_Phone', max_length=45, null=True, blank=True , verbose_name='Phone Number')
    RG_ID = models.CharField( db_column='RG_ID', max_length=45, null=True, blank=True, verbose_name='RG_ID')
    is_staff = models.BooleanField(db_column='is_staff', default=True)
    is_ref_physician_user = models.BooleanField(db_column='is_ref_physician', default=False, verbose_name='Referral Physician')
    is_radiologist_user = models.BooleanField(db_column='is_radiologist', default=False, verbose_name='Radiologist')
    is_admin = models.BooleanField(db_column='is_admin', default=False, verbose_name='Admin')
    is_superuser = models.BooleanField(db_column='is_superuser', default=False, verbose_name='Super Admin')
    is_active = models.BooleanField(db_column='is_active', default=True, verbose_name='Active')
    date_joined = models.DateTimeField(db_column='date_joined', default=timezone.now, verbose_name='Date Joined')

    visible = models.JSONField(default=list, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username if self.username else ''
    
    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
    
    