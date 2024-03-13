from rest_framework import serializers
from .models import User, FeedItem


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    # def create(self, validated_data):
    #     """Create and return a new user"""
    #     user = User.objects.create_user(**validated_data)
    #     return user


class FeedItemSerializer(serializers.ModelSerializer):
    """Serializes a feed item object"""
    class Meta:
        model = FeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        read_only_fields = ('user_profile',)

    def create(self, validated_data):
        """ Create and return a new feed item object """
        user = self.context['request'].user
        return FeedItem.objects.create(user_profile=user, **validated_data)
