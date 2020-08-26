from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.index_view, name='index_page'),
    path('main', views.Main_page.as_view(), name='main_page'),
    path('login', views.login, name='login'),

    # path('top/<int:top_id>', views.top_like, name='top_like'),
    # path('under/<int:under_id>', views.under_like, name='under_like'),
    # path('shoes/<int:shoes_id>', views.shoes_like, name='shoes_like'),

    # 위 경로와 같은데 값을 ajax 상에서 POST로 보내줌
    path('top_like', views.top_like, name='top_like'),
    path('under_like', views.under_like, name='under_like'),
    path('shoes_like', views.shoes_like, name='shoes_like'),
    path('before_selected/', views.Main_page.as_view(), name='main_page'),
    path('option_selected/', views.SelectOptions.as_view(), name='change_option'),
    path('recommend_result/', views.recommend, name='recommend'),
    # localhost:8000/
    # path('main/', views.style_recommend, name='style_recommend'),
]