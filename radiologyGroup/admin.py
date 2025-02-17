from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import RadiologyGroup

# Register your models here.
@admin.register(RadiologyGroup)
class RadiologyGroupAdmin(ModelAdmin):
    list_display = ('Rg_ID', 'Rg_Name', 'Rg_Members', 'created_at', 'updated_at')
    search_fields = ('Rg_ID', 'Rg_Name', 'Rg_Members')

    list_display_links = [
        'Rg_ID',
        'Rg_Name',
    ]
    ordering = ('created_at',)

    list_per_page = 15

    change_form_show_cancel_button = True


    search_help_text = "Search by Rg ID, Rg Name, Rg Members"
