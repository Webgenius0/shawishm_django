from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Studies

# Register your models here.
@admin.register(Studies)
class StudiesAdmin(ModelAdmin):
    list_display = ['study_ID', 'study_Inc_ID_string', 'study_uid','accession_no','study_uid_url','studydate','study_directory','procedure_name','proc_start','modality','received_date','machine_name','branch_name','report_url','images','series','status_reported','report_verifier','institution_name','study_bodyparts','radiologist_id','radiologist_name','othercomments','Pataints_Name','referral_physician','radiology_group']
    list_filter = ['branch_name', 'status_reported', 'institution_name',] 
    search_fields =['study_ID','branch_name','institution_name']

    list_display_links = [
        'study_Inc_ID_string',
        'study_ID',
        'study_uid',
    ]
    ordering = ('created_at',)

    list_per_page = 10

    change_form_show_cancel_button = True

    search_help_text = "Search by study ID, Branch name, Institution name"

    date_hierarchy = 'studydate'
    

    def Pataints_Name(self, obj):
        return obj.pat_inc_id_det.Pat_Name if obj.pat_inc_id_det else None

    def referral_physician(self, obj):
        return obj.ref_inc.Ref_Phy_Name if obj.ref_inc else None
    referral_physician.short_description = 'Referral Physician Name'
    

    def radiology_group(self, obj):
        return obj.radiology_group.Rg_Name if obj.radiology_group else None
    radiology_group.short_description = 'Radiology Group Name'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('pat_inc_id_det', 'ref_inc', 'radiology_group')







