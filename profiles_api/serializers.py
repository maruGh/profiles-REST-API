from rest_framework import serializers
from .models import User


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    # def create(self, validated_data):
    #     """Create and return a new user"""
    #     user = User.objects.create_user(**validated_data)
    #     return user
