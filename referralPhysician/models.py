from django.db import models

# Create your models here.
class Referralphysician(models.Model):
    Ref_Inc_ID = models.BigAutoField(db_column='Ref_inc_id', primary_key=True, editable=False , unique=True)  # Field name made lowercase.
    Ref_ID = models.CharField(db_column='Ref_ID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    Ref_Phy_Name = models.CharField(db_column='Ref_phy_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    Ref_Phy_Phone = models.CharField(db_column='Ref_phy_phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Ref_Phy_Name