from django import forms
from .models import ImageModel, ExpiringLink, ImageComment


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image_file', 'short_description']
        short_description = forms.CharField(required=False,
                                            widget=forms.Textarea)


class ImageCommentForm(forms.ModelForm):
    class Meta:
        model = ImageComment
        fields = '__all__'


class ExpiringLinkForm(forms.ModelForm):
    class Meta:
        model = ExpiringLink
        fields = ['name', 'expiration']
        # fields = '__all__'
