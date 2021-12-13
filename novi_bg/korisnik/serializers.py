from rest_framework import serializers
from korisnik.models import UserRegistration, UserLogin


# class UserRegistrationSerializer(serializers.Serializer):
#     id = serializers.IntegerField
#     email = serializers.CharField(max_length=30, required=True)
#     username = serializers.CharField(max_length=20, required=True)
#     password = serializers.CharField(max_length=50, required=True)
#
#     def create(self, validated_data):
#         return UserRegistration.objects.create(**validated_data)

# menjam Serializer klasu ModelSerializer klasom


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['id', 'email', 'username', 'password']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['username', 'password']
