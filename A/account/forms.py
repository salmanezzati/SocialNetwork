from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Your password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Your password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This username already exists')
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email already exists')
        return email

    def clean(self):
        cd = super().clean()
        pass1 = cd.get('password1')
        pass2 = cd.get('password2')

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError('Password must match')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Your password'}))
