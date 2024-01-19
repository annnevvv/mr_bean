from django import forms
from .models import ImageModel, ExpiringLink, ImageComment


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image_file', 'short_description']
        short_description = forms.CharField(required=False,
                                            widget=forms.Textarea)


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'short_description']


class ImageCommentForm(forms.ModelForm):
    class Meta:
        model = ImageComment
        fields = ['text']


class ExpiringLinkForm(forms.ModelForm):
    class Meta:
        model = ExpiringLink
        fields = ['name', 'expiration']
        # fields = '__all__'
