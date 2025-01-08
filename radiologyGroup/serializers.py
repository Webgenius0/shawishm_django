from rest_framework import serializers
from .models import RadiologyGroup


class RadiologyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyGroup
        fields = ['rg_inc_id', 'rg_id', 'rg_name', 'rg_members']