from rest_framework import serializers
from .models import RadiologyGroup


class RadiologyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyGroup
        fields = [
            'Rg_Inc_ID',
            'Rg_ID',
            'Rg_Name',
            'Rg_Members',
        ]
        read_only_fields = ['RG_Inc_ID']