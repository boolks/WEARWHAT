from django.db import models
from django.contrib.auth.models import AbstractUser


# 회원정보
class CustomUser(AbstractUser):
    # 추가할 필드 작성

    name = models.CharField(max_length=10, null=True)

    GENDERS = (
        ('M', '남성'),
        ('W', '여성'),
    )
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)

    STYLES = (
        ('FORMAL', "포멀"),
        ('CASUAL', "캐주얼")
    )
    fav_style = models.CharField(verbose_name='선호 스타일', max_length=6, choices=STYLES)


# 옷 정보
class Cloth(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cloth'
