from django import forms
from .models import userDetails, Profile

class userLogin(forms.ModelForm):
    class Meta:
            fields = ['email', 'password']
            model = userDetails

class profileDetails(forms.ModelForm):
    class Meta:
        fields = ['user', 'is_email_verified', 'email_token', 'profile_image']
        model = Profile