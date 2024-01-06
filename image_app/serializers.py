
from .models import ImageModel, ImageCommentModel

from rest_framework import serializers


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


class ImageCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCommentModel
        fields = '__all__'
