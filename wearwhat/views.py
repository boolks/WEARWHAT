from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# 옷 추천 메인페이지
def main_page(request):
    pass
    return render(request, 'wearwhat/main.html')


# @login_required
# def style_recommend(request):
#     pass
#     return render(request, 'wearwhat/recommend.html.html')
# Create your views here.
