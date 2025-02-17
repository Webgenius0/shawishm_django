from .models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username' , 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self , validated_data):

        try:
            validate_password(validated_data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        user = User.objects.create(
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'U_ID',
            'username',
            'U_fullname',
            'U_sex',
            'U_address',
            'U_phone',
            'U_Role',
            'RG_ID',
            'is_superuser',
            'is_admin',
            'is_ref_physician_user',
            'is_radiologist_user',
            'visible',
        ]

        extra_kwargs = {
            'password': {'read_only': True},
        }


