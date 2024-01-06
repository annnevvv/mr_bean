
from .models import Image, ImageComment

from rest_framework import serializers


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ImageCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComment
        fields = '__all__'
