from django import forms
from django.contrib.auth.hashers import make_password, BCryptSHA256PasswordHasher

from chat.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'avatar']  # Include any other fields you need

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving it
        user.password = make_password(self.cleaned_data['password'], b"4g6gv548", BCryptSHA256PasswordHasher.algorithm)
        if commit:
            user.save()
        return user
