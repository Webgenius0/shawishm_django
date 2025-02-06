from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Referralphysician

# Register your models here.
@admin.register(Referralphysician)
class ReferralphysicianAdmin(ModelAdmin):
    list_display = ('Ref_ID', 'Ref_Phy_Name', 'Ref_Phy_Phone', 'created_at', 'updated_at')
    search_fields = ('Ref_ID', 'Ref_Phy_Name', 'Ref_Phy_Phone')
    list_filter = ('Ref_ID', 'Ref_Phy_Name', 'Ref_Phy_Phone')

    list_display_links = [
        'Ref_ID',
        'Ref_Phy_Name',
    ]