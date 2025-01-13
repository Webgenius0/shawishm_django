from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Referralphysician

# Register your models here.
@admin.register(Referralphysician)
class ReferralphysicianAdmin(ModelAdmin):
    list_display = ('Ref_Inc_ID', 'Ref_ID', 'Ref_Phy_Name', 'Ref_Phy_Phone', 'created_at', 'updated_at')
    search_fields = ('Ref_Inc_ID', 'Ref_ID', 'Ref_Phy_Name', 'Ref_Phy_Phone')
    list_filter = ('Ref_Inc_ID', 'Ref_ID', 'Ref_Phy_Name', 'Ref_Phy_Phone', 'created_at', 'updated_at')