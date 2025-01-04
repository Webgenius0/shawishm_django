from rest_framework import serializers
from .models import Referralphysician

class ReferralPhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referralphysician
        fields = ['ref_inc_id', 'ref_id', 'ref_phy_name', 'ref_phy_phone']