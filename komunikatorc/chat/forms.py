from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", max_length=100, widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username         = forms.CharField(label="username", max_length=100)
    password         = forms.CharField(label="password", max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="confirm_password", max_length=100, widget=forms.PasswordInput)