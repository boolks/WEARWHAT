from django.db import models
from django.forms import PasswordInput
from django import forms

# Django 내장폼 이용하지 않고 내용을 숨길 수 있는 비밀번호폼 만드는 클래스 PasswordField와 PasswordModelField
class PasswordField(forms.CharField):
    widget = forms.PasswordInput


class PasswordModelField(models.CharField):
    def formfield(self, **kwargs):
        defaults = {'form_class':PasswordField}
        defaults.update(kwargs)
        return super(PasswordModelField, self).formfield(**defaults)

# 회원가입폼
class UserDetail(models.Model):
    # 아이디
    user_id = models.CharField(max_length=20)
    # 비밀번호
    password = PasswordModelField(max_length=50, default='1234')
    # 이름
    name = models.CharField(max_length=10, null=True)
    # 성별
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_CHOICES = ((GENDER_FEMALE, "여성"), (GENDER_MALE, "남성"))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    # 선호스타일
    STYLE_FORMAL = 'FM'
    STYLE_CASUAL = 'CS'
    STYLE_CHOICES = ((STYLE_FORMAL, "포멀"), (STYLE_CASUAL, "캐주얼"))
    fav_style = models.CharField(choices=STYLE_CHOICES, blank=True, max_length=2)
