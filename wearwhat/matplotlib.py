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
    top_hash_df = pd.DataFrame()
    under_hash_df = pd.DataFrame()
    shoes_hash_df = pd.DataFrame()
    # 각 class에서 pandas로 데이터 뽑아오기

    for hash_list in top_df['hashtag'].values.tolist():
        for hash_value in hash_list:
            series_obj = pd.Series(hash_value)
            top_hash_df = top_hash_df.append(series_obj, ignore_index=True)

    top_hash_df = top_hash_df.rename(columns={0: 'hashtag'})

    for hash_list in under_df['hashtag'].values.tolist():
        for hash_value in hash_list:
            series_obj = pd.Series(hash_value)
            under_hash_df = under_hash_df.append(series_obj, ignore_index=True)

    under_hash_df = under_hash_df.rename(columns={0: 'hashtag'})

    for hash_list in shoes_df['hashtag'].values.tolist():
        for hash_value in hash_list:
            series_obj = pd.Series(hash_value)
            shoes_hash_df = shoes_hash_df.append(series_obj, ignore_index=True)

    shoes_hash_df = shoes_hash_df.rename(columns={0: 'hashtag'})

    # 각 Dataframe 합치기
    # print(top_hash_df['hashtag'].value_counts().head())
    # print(under_hash_df['hashtag'].value_counts().head())
    # print(shoes_hash_df['hashtag'].value_counts().head())

    # setting seaborn default for plots
    sns.set()

    # Matplotlib에 맑은고딕 한글폰트 설정하기
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    # font property 가져오기
    font_prop = fm.FontProperties(fname=font_path).get_name()
    # Matplotlib 의 rc(run command) 명령을 사용해서 한글폰트 설정
    matplotlib.rc('font', family=font_prop)
    # 레이블 크기 조정
    matplotlib.rc('xtick', labelsize=15)
    matplotlib.rc('ytick', labelsize=20)

    figure, (axes1) = plt.subplots(nrows=1, ncols=1)
    figure.set_size_inches(14, 12)

    sns.countplot(data=top_hash_df, x='hashtag', ax=axes1)
    sns.countplot(data=top_hash_df, y='hashtag', palette="Set3", ax=axes1,
                  order=top_hash_df['hashtag'].value_counts().head(5).index)
    # 경로 <--------저기 보이는 자신의 images 폴더로 넣어야됨
    plt.savefig('C:/Users/82104/WEARWHAT/wearwhat/static/images/top_image.png')

    sns.countplot(data=under_hash_df, x='hashtag', ax=axes1)
    sns.countplot(data=under_hash_df, y='hashtag', palette="Set3", ax=axes1,
                  order=under_hash_df['hashtag'].value_counts().head(5).index)
    # 경로 <--------저기 보이는 자신의 images 폴더로 넣어야됨
    plt.savefig('C:/Users/82104/WEARWHAT/wearwhat/static/images/under_image.png')

    sns.countplot(data=shoes_hash_df, x='hashtag', ax=axes1)
    sns.countplot(data=shoes_hash_df, y='hashtag', palette="Set3", ax=axes1,
                  order=shoes_hash_df['hashtag'].value_counts().head(5).index)
    # 경로 <--------저기 보이는 자신의 images 폴더로 넣어야됨
    plt.savefig('C:/Users/82104/WEARWHAT/wearwhat/static/images/shoes_image.png')