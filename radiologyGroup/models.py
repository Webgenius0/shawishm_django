from django.db import models
from uuid import uuid4

# Create your models here.
class RadiologyGroup(models.Model):
    Rg_Inc_ID = models.BigAutoField(db_column='RG_Inc_ID', primary_key=True, editable=False , unique=True)  # Field name made lowercase.
    Rg_ID = models.IntegerField(db_column='RG_ID', blank=True, null=True)  # Field name made lowercase.
    Rg_Name = models.CharField(db_column='RG_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    Rg_Members = models.CharField(db_column='RG_Members', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Rg_Name if self.Rg_Name else ""
    
    def get_members(self):
        return self.Rg_Members
    
    class Meta:
        verbose_name = 'Radiology Group'
        verbose_name_plural = 'Radiology Group'