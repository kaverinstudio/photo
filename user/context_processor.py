from django import forms
from django.contrib.auth.forms import AuthenticationForm


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш логин'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'})


def link_login(request):
    return {'login_link': MyAuthenticationForm()}
