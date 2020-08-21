from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.Main_page.as_view(), name='main_page'),
    # path(r'^like/$', views.top_like, name='top_like'),
    path('top/<int:top_id>', views.top_like, name='top_like'),
    path('under/<int:under_id>', views.under_like, name='under_like'),
    path('shoes/<int:shoes_id>', views.shoes_like, name='shoes_like'),
    path('before_selected/', views.Main_page.as_view(), name='main_page'),
    path('option_selected/', views.SelectOptions.as_view(), name='change_option'),

    # localhost:8000/
    # path('main/', views.style_recommend, name='style_recommend'),
]