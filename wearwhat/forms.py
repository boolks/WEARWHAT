from django import forms
# 장고의 기본 user모델 import
from django.contrib.auth.models import User
# from .models import UserDetail

from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from .models import CustomUser


# 회원가입 폼(ID, PW, 성별, 선호스타일)
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'name', 'gender', 'fav_style')
        labels = {
            'username': '아이디',
            'name': '이름'
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'gender', 'fav_style')

