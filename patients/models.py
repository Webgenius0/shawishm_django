from django.db import models

# Create your models here.
class Patients(models.Model):
    Pat_Inc_ID = models.BigAutoField(db_column='Pat_inc_id', primary_key=True, editable=False , unique=True)
    Pat_Inc_ID_string = models.CharField(db_column='Pat_inc_id_string', max_length=50, blank=True, null=True)  # Field name made lowercase.
    Pat_ID = models.CharField(db_column='Pat_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    Pat_Name = models.CharField(db_column='Pat_name', max_length=70, blank=True, null=True)  # Field name made lowercase.
    Pat_Sex = models.CharField(db_column='Pat_sex', max_length=10, blank=True, null=True)  # Field name made lowercase.
    Pat_DOB = models.DateField(db_column='Pat_DOB', blank=True, null=True)  # Field name made lowercase.
    Pat_Phone = models.CharField(db_column='Pat_phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    Notes = models.TextField(db_column='Notes', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Pat_Name