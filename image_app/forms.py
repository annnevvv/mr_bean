from django import forms
from .models import Image, ExpiringLink


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image_file', 'short_description']
        short_description = forms.CharField(required=False,
                                            widget=forms.Textarea)


class ExpiringLinkForm(forms.ModelForm):
    class Meta:
        model = ExpiringLink
        fields = ['name', 'expiration']
        # fields = '__all__'
