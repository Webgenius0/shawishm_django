from rest_framework import serializers
from .models import RadiologyGroup


class RadiologyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyGroup
        fields = '__all__'