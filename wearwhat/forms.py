from django import forms
# 장고의 기본 user모델 import
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'last_name', 'first_name']