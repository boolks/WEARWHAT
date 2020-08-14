from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import (CustomUserCreationForm, CustomUserChangeForm)

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # list page
    list_display = ['username', 'gender', 'fav_style']


    # add page
    add_form = CustomUserCreationForm
    add_fieldsets = (
        ('ID & PASSWORD', {'fields': ('username', 'password1', 'password2')}),
        ('NAME', {'fields': 'name'}),
        ('PERSONAL INFO', {'fields': ('gender', 'fav_style')}),
    )
    # change page
    add_form = CustomUserChangeForm
    add_fieldsets = (
        ('ID & PASSWORD', {'fields': ('username', 'password1', 'password2')}),
        ('NAME', {'fields': 'name'}),
        ('PERSONAL INFO', {'fields': ('gender', 'fav_style')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)