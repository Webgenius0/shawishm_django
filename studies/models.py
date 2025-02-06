from django.db import models
from patients.models import Patients
from referralPhysician.models import Referralphysician
from radiologyGroup.models import RadiologyGroup

# Create your models here.
class Studies(models.Model):
    study_Inc_ID = models.AutoField(db_column='Study_Inc_ID', primary_key=True , unique=True)  # Field name made lowercase.
    study_Inc_ID_string = models.CharField(db_column='Study_Inc_ID_string', max_length=50, blank=True, null=True)  # Field name made lowercase.
    study_ID = models.CharField(db_column='Study_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    study_uid = models.CharField(db_column='Study_UID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    accession_no = models.CharField(db_column='Accession_no', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pat_inc_id_det = models.ForeignKey(Patients, models.DO_NOTHING, db_column='Pat_Inc_ID', blank=True, null=True , related_name='pat_inc_id_del')  # Field name made lowercase.
    study_description = models.CharField(db_column='Study_Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    study_uid_url = models.CharField(db_column='Study_uid_Url', max_length=200, blank=True, null=True)  # Field name made lowercase.
    studydate = models.DateField(db_column='StudyDate', blank=True, null=True)  # Field name made lowercase.
    study_directory = models.CharField(db_column='Study_Directory', max_length=550, blank=True, null=True)  # Field name made lowercase.
    ref_inc = models.ForeignKey(Referralphysician, models.DO_NOTHING, db_column='Ref_Inc_ID', blank=True, null=True , related_name='ref_inc')  # Field name made lowercase.
    procedure_name = models.CharField(db_column='Procedure_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    proc_start = models.DateTimeField(db_column='Proc_Start', blank=True, null=True)  # Field name made lowercase.
    modality = models.CharField(db_column='Modality', max_length=10, blank=True, null=True)  # Field name made lowercase.
    received_date = models.DateTimeField(db_column='Received_Date', blank=True, null=True)  # Field name made lowercase.
    machine_name = models.CharField(db_column='Machine_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    branch_name = models.CharField(db_column='Branch_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    report_url = models.CharField(db_column='Report_Url', max_length=200, blank=True, null=True)  # Field name made lowercase.
    images = models.IntegerField(db_column='Images', blank=True, null=True)  # Field name made lowercase.
    series = models.IntegerField(db_column='Series', blank=True, null=True)  # Field name made lowercase.
    status_reported = models.CharField(db_column='Status_Reported', max_length=25, blank=True, null=True)  # Field name made lowercase.
    report_verifier = models.CharField(db_column='Report_Verifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    institution_name = models.CharField(db_column='Institution_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    study_bodyparts = models.CharField(db_column='Study_BodyParts', max_length=200, blank=True, null=True)  # Field name made lowercase.
    radiologist_name = models.CharField(db_column='Radiologist_Name', max_length=70, blank=True, null=True)  # Field name made lowercase.
    radiologist_id = models.IntegerField(db_column='Radiologist_ID', blank=True, null=True)  # Field name made lowercase.
    radiology_group = models.ForeignKey( RadiologyGroup, models.DO_NOTHING, db_column='Radiology_Group', blank=True, null=True , related_name='radiology_group')  # Field name made lowercase.
    othercomments = models.CharField(db_column='OtherComments', max_length=450, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.study_ID
    
    class Meta:
        verbose_name = 'Studies'
        verbose_name_plural = 'Studies'