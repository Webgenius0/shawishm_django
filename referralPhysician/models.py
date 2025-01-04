from django.db import models

# Create your models here.
class Referralphysician(models.Model):
    ref_inc_id = models.PositiveBigIntegerField(db_column='Ref_inc_id', primary_key=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='Ref_ID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ref_phy_name = models.CharField(db_column='Ref_phy_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ref_phy_phone = models.CharField(db_column='Ref_phy_phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'referralphysician'