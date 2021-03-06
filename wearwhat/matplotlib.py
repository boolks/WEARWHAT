import pandas as pd
from .models import Top, Under, Shoes
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
# models.py 에서 생성한 각 class를 불러온다


def matplotlib_graph():
    top_df = pd.DataFrame(list(Top.objects.all().values()))
    under_df = pd.DataFrame(list(Under.objects.all().values()))
    shoes_df =pd.DataFrame(list(Shoes.objects.all().values()))
    total_df = pd.concat([top_df, under_df, shoes_df], ignore_index=True)
    total_hash_df = pd.DataFrame()
    # 각 class에서 pandas로 데이터 뽑아오기

    for hash_list in total_df['hashtag'].values.tolist():
        for hash_value in hash_list:
            series_obj = pd.Series(hash_value)
            total_hash_df = total_hash_df.append(series_obj, ignore_index=True)

    total_hash_df = total_hash_df.rename(columns={0: 'hashtag'})

    # setting seaborn default for plots
    sns.set(style='white')

    # Matplotlib에 맑은고딕 한글폰트 설정하기
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    # font property 가져오기
    font_prop = fm.FontProperties(fname=font_path).get_name()
    # Matplotlib 의 rc(run command) 명령을 사용해서 한글폰트 설정
    matplotlib.rc('font', family=font_prop)

    # 레이블 크기 조정
    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=10)

    # 그래프 개수 및 크기 조정
    figure, (axes1) = plt.subplots(nrows=1, ncols=1)
    figure.set_size_inches(20, 5)

    sns.countplot(data=total_hash_df, x='hashtag', palette="gray", ax=axes1,
                  order=total_hash_df['hashtag'].value_counts().head(10).index)
    sns.despine(left=True, bottom=True)
    plt.xlabel('')
    plt.ylabel('')

    # 경로 <--------저기 보이는 자신의 images 폴더로 넣어야됨
    plt.savefig('C:/Users/hoonnaam/WEARWHAT/wearwhat/static/images/tag_image.png')
