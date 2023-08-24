from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'u-border-0 u-border-white u-input u-input-rectangle u-radius-50 u-input-1', 'placeholder':'Введите имя'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'u-border-0 u-border-white u-input u-input-rectangle u-radius-50 u-input-1', 'placeholder':'Введите пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'u-border-0 u-border-white u-input u-input-rectangle u-radius-50 u-input-1', 'placeholder':'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-20'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'u-border-grey-10 u-grey-10 u-input u-input-rectangle u-radius-20'}))

class DateForm(forms.Form): 
    date = forms.DateField(label = 'Дата', widget=forms.DateInput(attrs={'class': 'u-input u-input-rectangle', 'placeholder': 'Дата'}))

class AddExpenseForm(forms.Form): 
    title = forms.CharField(label = 'Название траты', widget=forms.TextInput(attrs = {'class':"u-border-none u-input u-input-rectangle u-radius-10", 'placeholder': "Название траты"}))
    cost = forms.IntegerField(label = 'Цена', widget  = forms.TextInput(attrs = {'class':"u-border-none u-input u-input-rectangle u-radius-10", 'placeholder': "Цена"}))
    date = forms.DateField(label = 'Дата', widget = forms.TextInput(attrs = {'class':"u-border-none u-input u-input-rectangle u-radius-10", 'placeholder': "По умолчанию - сегодня"}), required=False)

class SettingsForm(forms.Form):
    day_limit = forms.IntegerField(label = 'Лимит в день(руб)', widget = forms.NumberInput(attrs = {'class': "form-control", 'placeholder': "Лимит в день"}))
    month_limit = forms.IntegerField(label = 'Лимит в месяц(руб)', widget = forms.TextInput(attrs = {'class': "form-control", 'placeholder': "Лимит в месяц"}))
    