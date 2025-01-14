from rest_framework import serializers
from .models import Referralphysician

class ReferralPhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referralphysician
        fields = [
            'Ref_Inc_ID',
            'Ref_ID',
            'Ref_Phy_Name',
            'Ref_Phy_Phone',
        ]
        read_only_fields = ['Ref_Inc_ID']