from django.contrib.auth.models import User

from rest_framework import serializers

from .models import ImageModel, ImageCommentModel


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


class ImageCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCommentModel
        fields = '__all__'
