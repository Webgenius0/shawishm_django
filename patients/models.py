from django.db import models
from uuid import uuid4

# Create your models here.
class Patients(models.Model):
    patients_id = models.UUIDField(primary_key=True, default=uuid4, editable=False , unique=True)
    pat_inc_id = models.PositiveBigIntegerField(db_column='Pat_inc_id' , unique=True)  # Field name made lowercase.
    pat_inc_id_string = models.CharField(db_column='Pat_inc_id_string', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pat_id = models.CharField(db_column='Pat_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pat_name = models.CharField(db_column='Pat_name', max_length=70, blank=True, null=True)  # Field name made lowercase.
    pat_sex = models.CharField(db_column='Pat_sex', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pat_dob = models.DateField(db_column='Pat_DOB', blank=True, null=True)  # Field name made lowercase.
    pat_phone = models.CharField(db_column='Pat_phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.pat_name