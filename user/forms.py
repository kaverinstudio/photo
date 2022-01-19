from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, PasswordInput, CharField, ValidationError
from .models import UserModel


class SignupForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш логин'})
        self.fields['email'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш email'})
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Повторите ввод пароля'})


class UserEditForm(ModelForm):
    password1 = CharField(min_length=6, label='Пароль', widget=PasswordInput)
    password2 = CharField(
        min_length=6, label='Повторите ввод пароля', widget=PasswordInput)
    phone = CharField(label='Телефон')
    city = CharField(label='Адрес доставки')

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'phone', 'city')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш email'})
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Повторите ввод пароля'})
        self.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваше имя'})
        self.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваша фамилия'})
        self.fields['phone'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш телефон'})
        self.fields['city'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш адрес доставки'})

    def clean_password2(self):
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')

        if len(pass1) == 0 and len(pass2) == 0:
            return pass2

        if pass1 == pass2:
            return pass2

        raise ValidationError('Пароли не совпадают')
