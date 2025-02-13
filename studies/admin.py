from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Studies

# Register your models here.
@admin.register(Studies)
class StudiesAdmin(ModelAdmin):
    list_display = ['study_ID', 'study_Inc_ID_string', 'study_uid','accession_no','study_uid_url','studydate','study_directory','procedure_name','proc_start','modality','received_date','machine_name','branch_name','report_url','images','series','status_reported','report_verifier','institution_name','study_bodyparts','radiologist_id','radiologist_name','othercomments','pat_inc_id_det','ref_inc','radiology_group']
    list_filter = ['branch_name', 'status_reported', 'institution_name',]
    search_fields =['study_ID', 'accession_no','modality','branch_name','institution_name']

    list_display_links = [
        'study_Inc_ID_string',
        'study_ID',
        'study_uid',
    ]
    ordering = ('created_at',)


