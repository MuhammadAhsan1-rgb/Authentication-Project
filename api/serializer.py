from rest_framework import serializers
from .models import Details
from django.contrib.auth.models import User

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email" ,"password"]
        extra_kwargs = {"password": {"write_only": True , "min_length": 8 }}
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
