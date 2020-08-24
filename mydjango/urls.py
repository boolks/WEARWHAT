"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings

from wearwhat import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wearwhat.urls')),
    # 로그인
    # path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    # 회원가입
    path('accounts/join/', views.SignUp.as_view(), name='join'),
    # 로그아웃
    # path('accounts/logout/', auth_views.LogoutView.as_view(), {'next': None}, name='logout'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), {'next': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('accounts/logout', views.logout, name='logout')
]
