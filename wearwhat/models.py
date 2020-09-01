from django.conf import settings
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

    liked_top = models.ManyToManyField('Top', related_name='liked_top', blank=True)
    like_under = models.ManyToManyField('Under', related_name='liked_under', blank=True)
    like_shoes = models.ManyToManyField('Shoes', related_name='liked_shoes', blank=True)

    class Meta:
        db_table = 'user'


# 옷 정보 - 상의
class Top(models.Model):
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    title = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    top_like_users = models.ManyToManyField(CustomUser, through='TopLikes', related_name='top_like_users')
    top_save = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='top_save')

    class Meta:
        managed = False
        db_table = 'clothes_top'


class TopLikes(models.Model):
    like_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    top_like = models.ForeignKey(Top, on_delete=models.CASCADE)
    likedate = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'top_likes'


# 옷 정보 - 하의
class Under(models.Model):
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    title = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    under_like_users = models.ManyToManyField(CustomUser, through='UnderLikes', related_name='under_like_users')
    under_save = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='under_save')

    class Meta:
        managed = False
        db_table = 'clothes_under'


class UnderLikes(models.Model):
    like_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    under_like = models.ForeignKey(Under, on_delete=models.CASCADE)
    like_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'under_likes'


# 옷 정보 - 신발
class Shoes(models.Model):
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    title = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shoes_like_users = models.ManyToManyField(CustomUser, through='ShoesLikes', related_name='shoes_like_users')
    shoes_save = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shoes_save')

    class Meta:
        managed = False
        db_table = 'clothes_shoes'


class ShoesLikes(models.Model):
    like_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shoes_like = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    like_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'shoes_likes'
