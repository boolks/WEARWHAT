from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.main_page, name='main_page'),
    # localhost:8000/
    # path('main/', views.style_recommend, name='style_recommend'),
]