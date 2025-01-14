from .models import Studies
from rest_framework import serializers
from patients.serializers import PatientsSerializer
from referralPhysician.serializers import ReferralPhysicianSerializer
from radiologyGroup.serializers import RadiologyGroupSerializer

from patients.models import Patients



class StudiesPOSTSerializer(serializers.ModelSerializer):
    pat_inc_id_det = PatientsSerializer(read_only=True)
    ref_inc = ReferralPhysicianSerializer(read_only=True)
    radiology_group = RadiologyGroupSerializer(read_only=True)

    class Meta:
        model = Studies
        fields = [
            'study_Inc_ID',
            'study_Inc_ID_string',
            'study_ID',
            'study_uid',
            'accession_no',
            'study_description',
            'study_uid_url',
            'studydate',
            'study_directory',
            'procedure_name',
            'proc_start',
            'modality',
            'received_date',
            'machine_name',
            'branch_name',
            'report_url',
            'images',
            'series',
            'status_reported',
            'report_verifier',
            'institution_name',
            'study_bodyparts',
            'radiologist_id',
            'radiologist_name',
            'othercomments',
            'pat_inc_id_det',
            'ref_inc', 
            'radiology_group'
        ]



class StudiesSerializer(serializers.ModelSerializer):
    
    pat_inc_id_det = PatientsSerializer(required=False)
    ref_inc = ReferralPhysicianSerializer(required=False)
    radiology_group = RadiologyGroupSerializer(required=False)
    class Meta:
        model = Studies
        fields = [
            'study_Inc_ID',
            'study_Inc_ID_string',
            'study_ID',
            'study_uid',
            'accession_no',
            'study_description',
            'study_uid_url',
            'studydate',
            'study_directory',
            'procedure_name',
            'proc_start',
            'modality',
            'received_date',
            'machine_name',
            'branch_name',
            'report_url',
            'images',
            'series',
            'status_reported',
            'report_verifier',
            'institution_name',
            'study_bodyparts',
            'radiologist_id',
            'radiologist_name',
            'othercomments',
            'pat_inc_id_det',
            'ref_inc', 
            'radiology_group'
        ]
        # read_only fields 
        read_only_fields = [
            'study_Inc_ID',
            'pat_inc_id_det',
            'ref_inc',
            'radiology_group',
        ]
    

    def update(self, instance, validated_data):

        patient_data = validated_data.pop('pat_inc_id_det', None)
        ref_data = validated_data.pop('ref_inc', None)
        radiology_group_data = validated_data.pop('radiology_group', None)

        if patient_data:
            if isinstance(patient_data, dict):
                patient_serializer = PatientsSerializer(instance.pat_inc_id_det, data=patient_data, partial=True)
                if patient_serializer.is_valid(raise_exception=True):
                    patient_serializer.save()

        if ref_data:
            if isinstance(ref_data, dict):  
                ref_serializer = ReferralPhysicianSerializer(instance.ref_inc, data=ref_data, partial=True)
                if ref_serializer.is_valid(raise_exception=True):
                    ref_serializer.save()


        if radiology_group_data:
            if isinstance(radiology_group_data, dict):
                radiology_group_serializer = RadiologyGroupSerializer(instance.radiology_group, data=radiology_group_data, partial=True)
                if radiology_group_serializer.is_valid(raise_exception=True):
                    radiology_group_serializer.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance


class MergepatientsSerializer(serializers.Serializer):
    pat_inc_id_det = serializers.IntegerField(write_only=True)  

    class Meta:
        model = Studies
        fields = ['pat_inc_id_det']

    def update(self, instance, validated_data):
        patient_id = validated_data.get('pat_inc_id_det')

        try:
            patient = Patients.objects.get(pk=patient_id)
        except Patients.DoesNotExist:
            raise serializers.ValidationError("Patient not found.")


        instance.pat_inc_id_det = patient
        instance.save()

        return instance
    