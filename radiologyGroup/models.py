from django.db import models
from uuid import uuid4

# Create your models here.
class RadiologyGroup(models.Model):
    radiology_group_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    rg_inc_id = models.PositiveBigIntegerField(db_column='RG_Inc_ID', unique=True)  # Field name made lowercase.
    rg_id = models.IntegerField(db_column='RG_ID', blank=True, null=True)  # Field name made lowercase.
    rg_name = models.CharField(db_column='RG_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rg_members = models.CharField(db_column='RG_Members', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.rg_name
    
    def get_members(self):
        return self.rg_members