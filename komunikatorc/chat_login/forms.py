from django import forms
from django.contrib.auth.hashers import make_password

from chat.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    username = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password', 'avatar']  # Include any other fields you need

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving it
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
