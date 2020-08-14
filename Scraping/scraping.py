import bs4
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import re

# url = 'https://store.musinsa.com/app/items/lists/001'    # 상의
# url = 'https://store.musinsa.com/app/items/lists/003'    # 하의
url = 'https://store.musinsa.com/app/items/lists/022'    # 스커트
# url = 'https://store.musinsa.com/app/items/lists/005'    # 신발
# url = 'https://store.musinsa.com/app/items/lists/020'    # 원피스
htp = 'https://store.musinsa.com/'
res = requests.get(url)
html = res.text
bs = BeautifulSoup(html, 'html.parser')
tag_lists = bs.select('.li_box .li_inner .list_img')
# print(len(tag_lists))
# tag_lists
# 상세 링크(상의)
cloth_list = []
cloth_lists = []
url2 = 'https:'
for idx, tag in enumerate(tag_lists):
    tag_img = tag.find('a')
    tag_url = tag_img['href']
    link = urljoin(htp, tag_url)
    cloth_list.append(link)

# 상세 페이지 get 요청
for cloth in cloth_list[:90]:  # 일단 5개만!
    cloth_dict = {}

    d_res = requests.get(cloth)
    d_html = d_res.text
    d_bs = BeautifulSoup(d_html, 'html.parser')

    # 옷 이름 파싱
    title = d_bs.select('div.right_contents span.product_title > span')[0].text
    cloth_dict['title'] = title

    # 옷 브랜드 파싱
    brand = d_bs.select('.product_info .item_categories > a')[2].text
    brand = re.sub('[\(\)]', '', brand)
    cloth_dict['brand'] = brand

    # season, gender 태그 파싱
    detail_lists = d_bs.select('ul.product_article li p.product_article_contents')
    detail_list = []
    for idx, detail in enumerate(detail_lists[1]):
        detail_dict = {}
        if isinstance(detail, bs4.element.Tag):
            content = detail.text
            content = content.replace(' ', '')
            content = content.replace('\t', '')
            matched = re.search(r'(\D+)', content)
            val = matched.group(1)
            # print(idx, val.strip())
            if idx == 1:
                cloth_dict['season'] = val.strip()
            elif idx == 5:
                cloth_dict['gender'] = val.strip()
            else:
                continue

    # 옷 색깔 파싱
    color = d_bs.select('div.product_info_table > table > tbody > tr > td')[0].text.strip()
    cloth_dict['color'] = color

    # 옷 카테고리 입력ㅋㅋㅋㅋ
    # cloth_dict['category'] = '상의'

    # 옷 이미지
    image = d_bs.select(".product_left #detail_bigimg .product-img img")
    #     print(image)
    for i in image:
        link = i['src']
        #         print(link)
        image_link = urljoin(url2, link)
        cloth_dict['img'] = image_link

    # 옷 링크
    cloth_dict['url'] = cloth

    # 옷 정보 리스트에 추가
    cloth_lists.append(cloth_dict)

print(len(cloth_lists))

# DataFrame 저장
import pandas as pd
import numpy as np
data_df = pd.DataFrame(columns=['title', 'brand', 'season', 'gender', 'color', 'category', 'img', 'url'])
for data in cloth_lists:
    series_obj = pd.Series(data)
    data_df = data_df.append(series_obj, ignore_index=True)

data_df.index = np.arange(1, len(data_df)+1)

data_df.head()
# DB 저장 (mariaDB)
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://python:"+"python"+"@localhost/cloth_db", encoding='utf-8')
con = engine.connect()
data_df.to_sql(name='cloth', con=engine, if_exists='replace', index=True, index_label='id')