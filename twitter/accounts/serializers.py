from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Profile


class ProfileFollowingSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(source='user', slug_field='username', read_only=True)
    class Meta:
        model = User
        fields = ['username']

class ProfileSerializer(serializers.ModelSerializer):
    following = ProfileFollowingSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['following']    

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'profile']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.create_user(username=username, password=password)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')