from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Studies
from patients.serializers import PatientsSerializer
from referralPhysician.serializers import ReferralPhysicianSerializer
from radiologyGroup.serializers import RadiologyGroupSerializer
from django.core.exceptions import ObjectDoesNotExist

from patients.models import Patients
from referralPhysician.models import Referralphysician
from radiologyGroup.models import RadiologyGroup


class StudiesSerializer(serializers.ModelSerializer):
    
    pat_inc_id_det = PatientsSerializer()
    ref_inc = ReferralPhysicianSerializer()
    radiology_group = RadiologyGroupSerializer()
    class Meta:
        model = Studies
        fields = [
            'study_inc_id',
            'study_inc_id_string',
            'study_id',
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
            'pat_inc_id_det',
            'ref_inc',
            'radiology_group',
        ]
        # read_only filds 
        read_only_fields = [
            'study_inc_id',
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
            elif isinstance(patient_data, int): 
                try:
                    patient = Patients.objects.get(id=patient_data)
                    instance.pat_inc_id_det = patient
                except Patients.DoesNotExist:
                    raise serializers.ValidationError({"pat_inc_id_det": "Patient with this ID does not exist."})

        if ref_data:
            if isinstance(ref_data, dict):  
                ref_serializer = ReferralPhysicianSerializer(instance.ref_inc, data=ref_data, partial=True)
                if ref_serializer.is_valid(raise_exception=True):
                    ref_serializer.save()
            elif isinstance(ref_data, int): 
                try:
                    instance.ref_inc = Referralphysician.objects.get(id=ref_data)
                except Referralphysician.DoesNotExist:
                    raise serializers.ValidationError({"ref_inc": "Referral physician with this ID does not exist."})


        if radiology_group_data:
            if isinstance(radiology_group_data, dict):
                radiology_group_serializer = RadiologyGroupSerializer(instance.radiology_group, data=radiology_group_data, partial=True)
                if radiology_group_serializer.is_valid(raise_exception=True):
                    radiology_group_serializer.save()
            elif isinstance(radiology_group_data, int):
                try:
                    instance.radiology_group = RadiologyGroup.objects.get(id=radiology_group_data)
                except RadiologyGroup.DoesNotExist:
                    raise serializers.ValidationError({"radiology_group": "Radiology group with this ID does not exist."})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
