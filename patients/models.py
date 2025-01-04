from django.db import models

# Create your models here.
class Patients(models.Model):
    pat_inc_id = models.PositiveBigIntegerField(db_column='Pat_inc_id', primary_key=True)  # Field name made lowercase.
    pat_inc_id_string = models.IntegerField(db_column='Pat_inc_id_string', blank=True, null=True)  # Field name made lowercase.
    pat_id = models.CharField(db_column='Pat_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pat_name = models.CharField(db_column='Pat_name', max_length=70, blank=True, null=True)  # Field name made lowercase.
    pat_sex = models.CharField(db_column='Pat_sex', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pat_dob = models.DateField(db_column='Pat_DOB', blank=True, null=True)  # Field name made lowercase.
    pat_phone = models.CharField(db_column='Pat_phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'patients'