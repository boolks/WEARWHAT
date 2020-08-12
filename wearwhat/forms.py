from django import forms
# 장고의 기본 user모델 import
from django.contrib.auth.models import User
from .models import UserDetail


# 회원가입 폼(ID, PW, 성별, 선호스타일)
class UserDetailForm(forms.ModelForm):
    class Meta:
        # UserDetail 모델을 사용
        model = UserDetail

        fields = ('user_id', 'password', 'name', 'gender', 'fav_style',)



