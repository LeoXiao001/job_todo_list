from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

import datetime

from .models import ToDoList, ToDoItem, Profile


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Passowrd',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)


class ListCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = {'list_name'}


class ItemCreateForm(forms.ModelForm):
    field_order = ['item_name', 'description', 'priority', 'due_date', 'notification']
    class Meta:
        model = ToDoItem
        fields = {'item_name', 'description', 'priority', 'due_date', 'notification'}
        widgets = {
            'description': forms.Textarea,
            'due_date': forms.DateInput,
            'priority': forms.Select,
            'notification': forms.CheckboxInput,
        }
