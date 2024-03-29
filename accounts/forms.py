from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .models import MyUser

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    
class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    
    

    def clean_email(self):
            User = get_user_model()
            email = self.cleaned_data.get('email') #1
            username = self.cleaned_data.get('username')
            #2 check if the email is unique, using the Django ORM
            if User.objects.filter(email=email):
                raise forms.ValidationError('Email address must be unique')
            return email
    
    def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
    
            if not password1 or not password2:
                raise ValidationError("Please confirm your password")
            
            if password1 != password2:
                raise ValidationError("Passwords must match")
            
            return password2
            
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password1', 'password2']