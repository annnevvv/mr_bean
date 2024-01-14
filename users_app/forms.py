from django import forms
from django.contrib.auth.models import User


from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'tier']

    # avatar = forms.ImageField(widget=forms.ClearableFileInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'tier']
