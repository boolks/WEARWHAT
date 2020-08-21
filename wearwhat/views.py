from urllib.parse import urlparse

from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.db.models import Q
import json
from django.http import HttpResponse

from .forms import CustomUserCreationForm, ChangeOptionForm
from .models import Top, Under, Shoes
import random

user = get_user_model()


# 회원가입
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# 옷 추천 메인페이지
class Main_page(View):
    template_name = 'wearwhat/main.html'

    def __init__(self):
        self.top_list = []
        self.under_list = []
        self.shoes_list = []
        self.cloth_top = []
        self.cloth_under = []
        self.cloth_shoes = []

    @property
    def getTop(self):
        return self.top_list

    @property
    def getUnder(self):
        return self.under_list

    @property
    def getShoes(self):
        return self.shoes_list

    @getTop.setter
    def setTop(self, tops):
        self.top_list = tops

    @getUnder.setter
    def setUnder(self, under):
        self.under_list = under

    @getShoes.setter
    def setShoes(self, shoes):
        self.shoes_list = shoes

    # 화면 뿌리기
    def get(self, request):
        # 리스트 뿌리기
        print('getTop: ', self.getTop)
        if not self.getTop or not self.getUnder or not self.getShoes:
            print('없으면 뿌려야되지 않냐')
            self.get_random_Top(request)
            self.get_random_Under(request)
            self.get_random_Shoes(request)
        else:
            pass
        # 리스트 뿌리기
        cloth_top = Top.objects.filter(id__in=self.getTop)
        cloth_under = Under.objects.filter(id__in=self.getUnder)
        cloth_shoes = Shoes.objects.filter(id__in=self.getShoes)

        # cloth_top = Top.objects.filter(id__in=self.get_random_Top(request))
        # cloth_under = Under.objects.filter(id__in=self.get_random_Under(request))
        # cloth_shoes = Shoes.objects.filter(id__in=self.get_random_Shoes(request))

        # 폼 뿌리기
        # form = ChangeOptionForm()
        # return render(request, self.template_name, {'top': cloth_top, 'bottom': cloth_under, 'shoes': cloth_shoes, 'form': form})
        print('클로즈탑', cloth_top)
        return render(request, self.template_name, {'top': cloth_top, 'bottom': cloth_under, 'shoes': cloth_shoes})

    # 요청받기
    def post(self, request, *args, **kwargs):
        # 폼 뿌리기
        # form = ChangeOptionForm()
        # 선택 변경 폼
        if request.method == 'POST':
            form = ChangeOptionForm(request.POST)
            # 폼 입력 후 처리 어떻게될지
            if form.is_valid():
                pass
                # cloth_top = Top.objects.filter(id__in=self.get_random_Top(request))
                # cloth_under = Under.objects.filter(id__in=self.get_random_Under(request))
                # cloth_shoes = Shoes.objects.filter(id__in=self.get_random_Shoes(request))
                # post = form.save(commit=False)
                # return redirect('main_page', pk=post.pk)
        else:
            form = ChangeOptionForm()

        return render(request, 'wearwhat/recommend_select.html', {'form': form})

    # 상의 랜덤출력 함수
    def get_random_Top(self, request):
        print("뿌려")
        top_id_list = []
        current_user = request.user

        if current_user.is_authenticated:
            gender = current_user.gender
        else:
            gender = 'F'

        if gender == 'M':
            for i in Top.objects.filter(Q(gender='남')|Q(gender='남,여')).values_list('id', flat=True):
                top_id_list.append(i)
            top_random = random.sample(top_id_list, 5)
            self.setTop = top_random
        else:
            for i in Top.objects.filter(Q(gender='여')|Q(gender='남,여')).values_list('id', flat=True):
                top_id_list.append(i)
            top_random = random.sample(top_id_list, 5)
            self.setTop = top_random
        print('여기가 처음 getTop', self.getTop)
        return self.getTop

    # 하의 랜덤출력 함수
    def get_random_Under(self, request):
        under_id_list = []
        current_user = request.user

        if current_user.is_authenticated:
            gender = current_user.gender
        else:
            gender = 'F'

        if gender == 'M':
            for i in Under.objects.filter(Q(gender='남')|Q(gender='남,여')).values_list('id', flat=True):
                under_id_list.append(i)
            under_random = random.sample(under_id_list, 5)
            self.setUnder = under_random
        else:
            for i in Under.objects.filter(Q(gender='여')|Q(gender='남,여')).values_list('id', flat=True):
                under_id_list.append(i)
            under_random = random.sample(under_id_list, 5)
            self.setUnder = under_random
        return self.getUnder


    # 신발 랜덤출력 함수
    def get_random_Shoes(self, request):
        shoes_id_list = []
        current_user = request.user

        if current_user.is_authenticated:
            gender = current_user.gender
        else:
            gender = 'F'

        if gender == 'M':
            for i in Shoes.objects.filter(Q(gender='남')|Q(gender='남,여')).values_list('id', flat=True):
                shoes_id_list.append(i)
            shoes_random = random.sample(shoes_id_list, 5)
            self.setShoes = shoes_random
        else:
            for i in Shoes.objects.filter(Q(gender='여')|Q(gender='남,여')).values_list('id', flat=True):
                shoes_id_list.append(i)
            shoes_random = random.sample(shoes_id_list, 5)
            self.setShoes = shoes_random
        return self.getShoes



def top_like(request):
    top_id = request.POST.get('top_id', None)
    like = get_object_or_404(Top, id=top_id)

    if request.user in like.top_like_users.all():
        like.top_like_users.remove(request.user)
        like_icon = False
    else:
        like.top_like_users.add(request.user)
        like_icon = True

    context = {'like_count':like.top_like_users.count(), 'like_icon':like_icon}
    return HttpResponse(json.dumps(context), content_type="application/json")


def under_like(request):
    under_id = request.POST.get('under_id', None)
    like = get_object_or_404(Under, id=under_id)

    if request.user in like.under_like_users.all():
        like.under_like_users.remove(request.user)
        like_icon = False
    else:
        like.under_like_users.add(request.user)
        like_icon = True

    context = {'like_count':like.under_like_users.count(), 'like_icon':like_icon}
    return HttpResponse(json.dumps(context), content_type="application/json")

def shoes_like(request):
    shoes_id = request.POST.get('shoes_id', None)
    like = get_object_or_404(Shoes, id=shoes_id)

    if request.user in like.shoes_like_users.all():
        like.shoes_like_users.remove(request.user)
        like_icon = False
    else:
        like.shoes_like_users.add(request.user)
        like_icon = True

    context = {'like_count':like.shoes_like_users.count(), 'like_icon':like_icon}
    return HttpResponse(json.dumps(context), content_type="application/json")

# 선호 스타일, 장소나 목적 선택하면 옷 리스트 다시 뿌려줌
class SelectOptions(Main_page):
    template_name = 'wearwhat/recommend_select.html'

    def get(self, request):
        super().get(request)
        cloth_top = Top.objects.filter(id__in=self.get_random_Top(request))
        cloth_under = Under.objects.filter(id__in=self.get_random_Under(request))
        cloth_shoes = Shoes.objects.filter(id__in=self.get_random_Shoes(request))

        form = ChangeOptionForm()
        return render(request, self.template_name,
                      {'top': cloth_top, 'bottom': cloth_under, 'shoes': cloth_shoes, 'form': form})
