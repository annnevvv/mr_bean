from django import forms
from .models import ImageModel, ExpiringLinkModel


class UploadedImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image_file', 'short_description']
        short_description = forms.CharField(required=False,
                                            widget=forms.Textarea)


class ExpiringLinkForm(forms.ModelForm):
    class Meta:
        model = ExpiringLinkModel
        fields = ['name', 'expiration']
        # fields = '__all__'
