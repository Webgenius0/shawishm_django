from rest_framework import serializers
from .models import Patients

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = [
            'Pat_Inc_ID',
            'Pat_Inc_ID_string',
            'Pat_ID',
            'Pat_Name',
            'Pat_Sex',
            'Pat_DOB',
            'Pat_Phone',
            'Notes',
        ]
        read_only_fields = ['Pat_Inc_ID']