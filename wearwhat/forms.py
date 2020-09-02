from django import forms
# 장고의 기본 user모델 import
from django.contrib.auth.models import User
# from .models import UserDetail

from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from .models import CustomUser

STYLES = [
    ('FORMAL', "포멀"),
    ('CASUAL', "캐주얼")
]
FORWHERE = [
    ('SCHOOL', "학교"),
    ('WORK', "직장"),
    ('DATE', "데이트")
]


class ChangeOptionForm(forms.Form):
    fav_style_change = forms.ChoiceField(label="스타일",
                                         choices=STYLES,
                                         widget=forms.Select(attrs={'class': 'form-control-lg'}))
    for_where = forms.ChoiceField(label="어디",
                                  choices=FORWHERE,
                                  widget=forms.Select(attrs={'class': 'form-control-lg'}))


# 회원가입 폼(ID, PW, 성별, 선호스타일)
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'name', 'gender', 'fav_style')
        labels = {
            'username': '아이디',
            'name': '이름'
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }



# admin page 정보수정 폼
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'gender', 'fav_style')
