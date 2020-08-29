from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse
from django.db.models import Count
from django.contrib import auth

from .forms import CustomUserCreationForm, ChangeOptionForm
from .models import Top, Under, Shoes

import random
import json
from pyowm import OWM

user = get_user_model()


# 현재 온도 추출 함수
def get_temperature():
    owm = OWM('b00d21f228833645831c1f84465ca689')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Seoul,KR')
    temp = observation.weather.temperature('celsius').get('temp')
    weather = observation.weather.status
    # print('현재날씨: ', weather)
    # print('현재온도: ', temperature)
    return temp, weather


temp, weather = get_temperature()
weather = weather.lower()
# print('온도:', temp)
print('날씨:', weather)



# 로그인 전 메인페이지
def index_view(request):
    # DB 옷 데이터 개수
    top_count = Top.objects.all().aggregate(Count('id')).get('id__count')
    under_count = Under.objects.all().aggregate(Count('id')).get('id__count')
    shoes_count = Shoes.objects.all().aggregate(Count('id')).get('id__count')
    cloth_count = top_count + under_count + shoes_count

    # 로그인 전 => index 페이지 / 로그인 완료 => main 페이지
    current_user = request.user
    if current_user.is_authenticated:
        # return_url = reverse_lazy('main_page')
        return HttpResponseRedirect(reverse('main_page'))
    else:
        # return_url = reverse_lazy('index_page')
        return render(request, 'wearwhat/index.html', {'cloth_count': cloth_count})


# 로그인
def login(request):
    if request.method == 'POST':
        # post 요청이 들어온다면
        # print('유저네임', request.POST['username'])
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(request, username=username, password=password)
        # 입력받은 아이디와 비밀번호가 데이터베이스에 존재하는지 확인.
        if user is not None:
            # 데이터 베이스에 회원정보가 존재한다면 로그인 시키고 home으로 돌아가기.
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main_page'))
        else:
            # 회원정보가 존재하지 않는다면, 에러인자와 함께 login 템플릿으로 돌아가기.
            return render(request, 'registration/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'registration/login.html')


# 회원가입
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# 옷 추천 메인페이지
class Main_page(View):
    template_name = 'wearwhat/main.html'

    # 화면 뿌리기
    def get(self, request):
        current_user = request.user
        if current_user.is_authenticated:
            # 리스트 뿌리기
            cloth_top = Top.objects.filter(id__in=get_random_Top(request))
            cloth_under = Under.objects.filter(id__in=get_random_Under(request))
            cloth_shoes = Shoes.objects.filter(id__in=get_random_Shoes(request))

            return render(request, self.template_name,
                          {'top': cloth_top, 'under': cloth_under, 'shoes': cloth_shoes, 'temp': temp, 'weather': weather})
        else:
            return render(request, 'wearwhat/index.html')

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
def get_random_Top(request):
    top_id_list = []
    
    current_user = request.user
    
    style = current_user.fav_style
    if style == 'FORMAL':
        style = '포멀'
    elif style == 'CASUAL':
        style = '캐주얼'
        
    gender = current_user.gender
    if gender == 'M':
        gender = '남'
    else:
        gender = '여'

    # 현재 온도 >= 23 인 경우 반팔만
    if temp >= 24:
        exclude_list = [17, 20]

    # 23 < 현재 온도 < 27 인 경우 얇은긴팔ㅇㅋ
    elif 17 < temp < 24:
        exclude_list = [17]

    # 현재 온도 <= 17 인 경우 얇은 옷 제외
    elif temp < 17:
        exclude_list = [27, 23, 20]

    for i in Top.objects.exclude(temperature__in=exclude_list). \
            filter(Q(gender=gender) | Q(gender='남,여')).filter(style=style).values_list('id', flat=True):
        top_id_list.append(i)
    top_random = random.sample(top_id_list, 5)
    return top_random


# 하의 랜덤출력 함수
def get_random_Under(request):
    under_id_list = []
    
    current_user = request.user
    
    style = current_user.fav_style
    if style == 'FORMAL':
        style = '포멀'
    elif style == 'CASUAL':
        style = '캐주얼'
        
    gender = current_user.gender
    if gender == 'M':
        gender = '남'
    else:
        gender = '여'

    # 현재 온도 >= 23 인 경우
    if temp >= 24:
        exclude_list = [17, 20]

    # 23 < 현재 온도 < 27 인 경우
    elif 17 < temp < 24:
        exclude_list = [17]

    # 현재 온도 <= 17 인 경우
    elif temp < 17:
        exclude_list = [27, 23]

    for i in Under.objects.exclude(temperature__in=exclude_list). \
            filter(Q(gender=gender) | Q(gender='남,여')).values_list('id', flat=True):
        under_id_list.append(i)
    under_random = random.sample(under_id_list, 5)
    return under_random


# 신발 랜덤출력 함수
def get_random_Shoes(request):
    shoes_id_list = []
    
    current_user = request.user
    
    style = current_user.fav_style
    if style == 'FORMAL':
        style = '포멀'
    elif style == 'CASUAL':
        style = '캐주얼'

    gender = current_user.gender
    if gender == 'M':
        gender = '남'
    else:
        gender = '여'

    # 현재 온도 >= 23 인 경우
    if temp >= 24:
        exclude_list = [17, 20]

    # 23 < 현재 온도 < 27 인 경우
    elif 17 < temp < 24:
        exclude_list = [17]

    # 현재 온도 <= 17 인 경우
    elif temp < 17:
        exclude_list = [27, 23]

    for i in Shoes.objects.exclude(temperature__in=exclude_list). \
            filter(Q(gender=gender) | Q(gender='남,여')).filter(style=style).values_list('id', flat=True):
        shoes_id_list.append(i)
    shoes_random = random.sample(shoes_id_list, 5)
    return shoes_random

# 상의 좋아요
def top_like(request):
    # html로 부터 top_id를 받아옴
    top_id = request.POST.get('top_id', None)
    like = get_object_or_404(Top, id=top_id)

    # top_id에 해당하는 상의에 현재 유저가 좋아요를 이미 눌렀을 경우 제거
    if request.user in like.top_like_users.all():
        like.top_like_users.remove(request.user)
        like_icon = False
    else:
        like.top_like_users.add(request.user)
        like_icon = True

    # 카운트 수와 좋아요의 여부를 key:value 형식(json) 으로 묶어 리턴
    context = {'like_count': like.top_like_users.count(), 'like_icon': like_icon}
    return HttpResponse(json.dumps(context), content_type="application/json")


# 하의 좋아요
def under_like(request):
    under_id = request.POST.get('under_id', None)
    like = get_object_or_404(Under, id=under_id)

    if request.user in like.under_like_users.all():
        like.under_like_users.remove(request.user)
        like_icon = False
    else:
        like.under_like_users.add(request.user)
        like_icon = True

    context = {'like_count': like.under_like_users.count(), 'like_icon': like_icon}
    return HttpResponse(json.dumps(context), content_type="application/json")


# 신발 좋아요
def shoes_like(request):
    shoes_id = request.POST.get('shoes_id', None)
    like = get_object_or_404(Shoes, id=shoes_id)

    if request.user in like.shoes_like_users.all():
        like.shoes_like_users.remove(request.user)
        like_icon = False
    else:
        like.shoes_like_users.add(request.user)
        like_icon = True

    context = {'like_count': like.shoes_like_users.count(), 'like_icon': like_icon}
    return HttpResponse(json.dumps(context), content_type="application/json")


# 선호 스타일, 장소나 목적 선택하면 옷 리스트 다시 뿌려줌
class SelectOptions(Main_page):
    template_name = 'wearwhat/recommend_select.html'

    def get(self, request):
        super().get(request)
        cloth_top = Top.objects.filter(id__in=get_random_Top(request))
        cloth_under = Under.objects.filter(id__in=get_random_Under(request))
        cloth_shoes = Shoes.objects.filter(id__in=get_random_Shoes(request))

        form = ChangeOptionForm()
        return render(request, self.template_name,
                      {'top': cloth_top, 'under': cloth_under, 'shoes': cloth_shoes, 'form': form})


# 추천 받는 메소드 구현중 위에거랑 합치든 해야댐
def recommend(request):
    current_user = request.user
    template_name = 'wearwhat/recommend_result.html'
    if request.method == "POST":
        form = ChangeOptionForm(request.POST)

        if form.is_valid():
            # fav_style_change = form.cleaned_data['fav_style_change']
            for_where = form.cleaned_data['for_where']
            if for_where == 'SCHOOL':
                current_user.fav_style = 'CASUAL'
            elif for_where == 'WORK':
                current_user.fav_style = 'FORMAL'
            else:
                current_user.fav_style = 'ALL'

            cloth_top = Top.objects.filter(id__in=get_random_Top(request))
            cloth_under = Under.objects.filter(id__in=get_random_Under(request))
            cloth_shoes = Shoes.objects.filter(id__in=get_random_Shoes(request))

            return render(request, template_name,
                          {'top': cloth_top, 'under': cloth_under, 'shoes': cloth_shoes})


# 상의 결과 선택
def top_choice(request):
    # html로 부터 top_id를 받아옴
    top_id = request.POST.get('top_id', None)
    choice = get_object_or_404(Top, id=top_id)

    # top_id에 해당하는 상의에 현재 유저가 좋아요를 이미 눌렀을 경우 제거
    img = choice.image

    # 카운트 수와 좋아요의 여부를 key:value 형식(json) 으로 묶어 리턴
    context = {'img': img}
    return HttpResponse(json.dumps(context), content_type="application/json")

# 하의 결과 선택
def under_choice(request):
    # html로 부터 top_id를 받아옴
    under_id = request.POST.get('under_id', None)
    choice = get_object_or_404(Under, id=under_id)

    # top_id에 해당하는 상의에 현재 유저가 좋아요를 이미 눌렀을 경우 제거
    img = choice.image

    # 카운트 수와 좋아요의 여부를 key:value 형식(json) 으로 묶어 리턴
    context = {'img': img}
    return HttpResponse(json.dumps(context), content_type="application/json")

# 신발 결과 선택
def shoes_choice(request):
    # html로 부터 top_id를 받아옴
    shoes_id = request.POST.get('shoes_id', None)
    choice = get_object_or_404(Shoes, id=shoes_id)

    # top_id에 해당하는 상의에 현재 유저가 좋아요를 이미 눌렀을 경우 제거
    img = choice.image

    # 카운트 수와 좋아요의 여부를 key:value 형식(json) 으로 묶어 리턴
    context = {'img': img}
    return HttpResponse(json.dumps(context), content_type="application/json")


def logout(request):
    auth.logout(request)
    return redirect('/')
