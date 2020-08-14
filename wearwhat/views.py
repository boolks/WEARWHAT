from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .models import Cloth


# 회원가입
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# 옷 추천 메인페이지
def main_page(request):
    pass
    cloth = Cloth.objects.all()
    return render(request, 'wearwhat/main.html', {'cloth': cloth})


