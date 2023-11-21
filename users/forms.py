from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Optional.')
    real_name = forms.CharField(max_length=10, required=True, help_text='Required. Enter your first name.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'real_name', 'phone_number')
        
        