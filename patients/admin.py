from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Patients

# Register your models here.
@admin.register(Patients)
class PatientsAdmin(ModelAdmin):
    list_display = ('Pat_Inc_ID', 'Pat_Inc_ID_string', 'Pat_ID', 'Pat_Name', 'Pat_Sex', 'Pat_DOB', 'Pat_Phone', 'Notes', 'created_at', 'updated_at')
    search_fields = ('Pat_Inc_ID', 'Pat_Inc_ID_string','Pat_ID', 'Pat_Name','Pat_Phone')
    list_filter = ('Pat_Inc_ID', 'Pat_Inc_ID_string','Pat_ID', 'Pat_Name', 'Pat_Sex', 'Pat_DOB', 'Pat_Phone', 'Notes', 'created_at', 'updated_at')