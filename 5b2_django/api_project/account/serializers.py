from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        
    def create(self, validated_data):
        print("This is the serializer that we are using")
        return super().create(validated_data)
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=500)