from email.policy import default
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


employment_type = (
    ('1', 'Employee'),
    ('2', 'Intern'),
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', required=True)
    type = forms.ChoiceField(choices=employment_type)

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'type',
            'password1',
            'password2',
        }

        labels = {
            'username' : 'Username',
            'first_name': 'Name',
            'last_name': 'Last Name',
            'password1' : 'Password',
            'password2' : 'Confirm Password',
        }
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.type = self.cleaned_data['type']
        user.email = self.cleaned_data['email']
        em_type = self.cleaned_data['type']

        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user, type = em_type)
            user_profile.save()

        return user

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['placeholder'] = 'Employment-Type'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'
        
        
class ProfilePictureForm(forms.Form):
    img = forms.ImageField()
    class Meta:
        model = UserProfile
        fields = ['img']

    def save(self, request, commit=True):
        user = request.user.userprofile_set.first()
        user.img = self.cleaned_data['img']

        if commit:
            user.save()

        return user

    def __init__(self, *args, **kwargs):
        super(ProfilePictureForm, self).__init__(*args, **kwargs)
        self.fields['img'].widget.attrs['class'] = 'custom-file-input'
        self.fields['img'].widget.attrs['id'] = 'validatedCustomFile'