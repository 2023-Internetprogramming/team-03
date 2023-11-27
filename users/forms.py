from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Optional.')
    real_name = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'real_name', 'phone_number')
        

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'real_name']       