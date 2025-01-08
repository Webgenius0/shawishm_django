from rest_framework import serializers
from .models import Patients

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['pat_inc_id', 'pat_inc_id_string', 'pat_id', 'pat_name', 'pat_sex', 'pat_dob', 'pat_phone', 'notes']