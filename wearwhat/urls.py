from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.Main_page.as_view(), name='main_page'),
    # path('top/<int:top_id>', views.top_like, name='top_like'),
    # path('under/<int:under_id>', views.under_like, name='under_like'),
    # path('shoes/<int:shoes_id>', views.shoes_like, name='shoes_like'),
    # 위 경로와 같은데 값을 ajax 상에서 POST로 보내줌
    path(r'^top_like/$', views.top_like, name='top_like'),
    path(r'^under_like/$', views.under_like, name='under_like'),
    path(r'^shoes_like/$', views.shoes_like, name='shoes_like'),
    path('before_selected/', views.Main_page.as_view(), name='main_page'),
    path('option_selected/', views.SelectOptions.as_view(), name='change_option'),

    # localhost:8000/
    # path('main/', views.style_recommend, name='style_recommend'),
]