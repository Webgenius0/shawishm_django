from rest_framework import serializers
from .models import Studies
from patients.serializers import PatientsSerializer
from referralPhysician.serializers import ReferralPhysicianSerializer
from radiologyGroup.serializers import RadiologyGroupSerializer


class StudiesSerializer(serializers.ModelSerializer):
    pat_inc_id_det= PatientsSerializer(read_only=True)
    ref_inc = ReferralPhysicianSerializer(read_only=True)
    radiology_group = RadiologyGroupSerializer(read_only=True)
    class Meta:
        model = Studies
        fields = '__all__'
        extra_kwargs = {
            'study_inc_id': {'read_only': True},
        }