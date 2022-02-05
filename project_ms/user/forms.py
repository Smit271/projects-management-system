from dataclasses import field
from wsgiref.validate import validator
from django import forms
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
            'email_id'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
            'first_name'    : forms.TextInput(attrs = {'placeholder': 'First Name'}),
            'last_name'    : forms.TextInput(attrs = {'placeholder': 'Last Name'}),
            'confirm_pass'    : forms.PasswordInput(attrs = {'placeholder': 'Confirm Password'}),
            'password': forms.PasswordInput(attrs= {'placeholder' : 'Password'})
        }