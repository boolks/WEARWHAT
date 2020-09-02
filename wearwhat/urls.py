from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.index_view, name='index_page'),
    path('main', views.Main_page.as_view(), name='main_page'),
    path('login', views.login, name='login'),

    # 위 경로와 같은데 값을 ajax 상에서 POST로 보내줌
    path('top_like', views.top_like, name='top_like'),
    path('under_like', views.under_like, name='under_like'),
    path('shoes_like', views.shoes_like, name='shoes_like'),
    path('before_selected/', views.Main_page.as_view(), name='main_page'),
    path('option_selected/', views.SelectOptions.as_view(), name='change_option'),
    path('recommend_result/', views.recommend, name='recommend'),
    path('top_choice', views.top_choice, name='top_choice'),
    path('under_choice', views.under_choice, name='under_choice'),
    path('shoes_choice', views.shoes_choice, name='shoes_choice'),
    path('item_save', views.item_save, name='item_save'),
    path('my_choice', views.my_choice.as_view(), name='my_choice'),
    path('top_remove', views.top_remove, name='top_remove'),
    path('under_remove', views.under_remove, name='under_remove'),
    path('shoes_remove', views.shoes_remove, name='shoes_remove'),
]