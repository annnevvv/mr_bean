from django.contrib.auth.models import User

from rest_framework import serializers

from .models import UserAccountTier, UserProfileModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'date_joined']


class UserAccountTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccountTier
        fields = '__all__'


class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = '__all__'
