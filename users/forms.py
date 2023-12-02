from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
import re

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Optional.')
    real_name = forms.CharField(max_length=10, required=True)
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not re.match(r'^010-\d{4}-\d{4}$', phone_number):
            raise forms.ValidationError('올바른 전화번호 형식이 아닙니다. (예: 010-XXXX-XXXX)')

        return phone_number

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'real_name', 'phone_number')
        

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'real_name']       