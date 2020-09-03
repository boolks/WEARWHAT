from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import re
import pymongo
import json
url_base = 'https://store.musinsa.com/app/items/lists/'
url_list = ['001', '003', '022', '020', '005']  # 상의, 하의, 스커트, 원피스, 신발
# seq_num = 0
top_total = 0
under_total = 0
for url in url_list:  # 0: 상의, 1: 하의:, 2:스커트, 3:원피스, 4:신발
    cloth_total = []
    url_final = 'https://store.musinsa.com/app/items/lists/' + url + '/?category=&d_cat_cd=001&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=500&page=1'
    htp = 'https://store.musinsa.com/'
    res = requests.get(url_final)
    html = res.text
    bs = BeautifulSoup(html, 'html.parser')
    tag_lists = bs.select('.li_box .li_inner .list_img')
    # print(len(tag_lists))
    cloth_list = []
    # 상세 링크
    url2 = 'https:'
    for tag in tag_lists:
        tag_img = tag.find('a')
        tag_url = tag_img['href']
        link = urljoin(htp, tag_url)
        cloth_list.append(link)
    # 상세 페이지 get 요청
    for index, cloth in enumerate(cloth_list[:10], 1):  # 일단 5개만!
        d_res = requests.get(cloth)
        d_html = d_res.text
        d_bs = BeautifulSoup(d_html, 'html.parser')
        cloth_dict = {}
        # id(순서, 고유값) 파싱
        # if url == '020' or url == '022':
        #     index2 = seq_num + index
        #     cloth_dict['id'] = index2
        # else:
        #     cloth_dict['id'] = index
        if url == '020':
            total = top_total + index
            cloth_dict['id'] = total
        elif url == '022':
            total = under_total + index
            cloth_dict['id'] = total
        else:
            cloth_dict['id'] = index
        
        # 인덱스 번호가 아닌 옷의 고유 id를 찾아 저장하는 방법 -> 여러 페이지에서 스크랩할 땐 겹칠 수 있어서 불리
        # matched = re.search(r'\d+[^/0]', cloth)
        # cloth_id = int(matched.group())
        # cloth_dict['id'] = cloth_id
        
        # 옷 이름 파싱
        title = d_bs.select('div.right_contents span.product_title > span')[-1].text
        cloth_dict['title'] = title
        # 옷 브랜드 파싱
        brand = d_bs.select('.product_info .item_categories > a')[2].text
        brand = re.sub('[\(\)]', '', brand)
        cloth_dict['brand'] = brand
        # Season 파싱
        detail_lists = d_bs.select(
            'div.explan_product > ul.product_article > li:nth-of-type(2)  p.product_article_contents > strong')
        if not detail_lists:
            pass
        else:
            if detail_lists[0].text == '원':
                cloth_dict['season'] = 'ALL'
            else:
                content = detail_lists[0].text.strip()
                content = content.replace('\t', '')
                # print(content)
                cloth_dict['season'] = content.strip()
        # 성별 파싱
        genders = d_bs.select('ul.product_article > li p.product_article_contents .txt_gender')
        gender_list = []
        for gender in genders:
            gender_list.append(gender.text.strip().replace('\n', ','))
            cloth_dict['gender'] = gender_list
        # 옷 색깔 파싱
        color = d_bs.select('div.product_info_table > table > tbody > tr > td')[0].text.strip()
        cloth_dict['color'] = color
        # 옷 카테고리 파싱
        category = d_bs.select('.product_info .item_categories > a')[0].text
        cloth_dict['category'] = category
        # 옷 카테고리2(detail) 파싱
        detail_category = d_bs.select('.product_info .item_categories > a')[1].text
        cloth_dict['detail'] = detail_category
        # 해시태그 파싱
        hashtag = d_bs.select(".product_article .article-tag-list .product_article_contents ")
        hash_list = []
        for tag in hashtag:
            hash_list = tag.text.split("\n")
        cloth_dict['hashtag'] = hash_list[1:len(hash_list) - 1]
        # 옷 이미지 파싱
        image = d_bs.select(".product_left #detail_bigimg .product-img img")
        for i in image:
            link = i['src']
            image_link = urljoin(url2, link)  # http 프로토콜 포함시켜줌
            cloth_dict['image'] = image_link
        # 옷 링크 파싱
        cloth_dict['url'] = cloth
        # 옷 정보 리스트에 추가
        cloth_total.append(cloth_dict)
        print(f'{url}, {index} 번째 진행중')
    print(len(cloth_total))

    print(cloth_total)
    if url == '020':
        url = '001'
        # seq_num = 0
    elif url == '022':
        url = '003'
        # seq_num = 0
    with open('cloth' + url + '.json', 'w', encoding='utf8') as file:
        json.dump(cloth_total, file)
    # print('json file write 종료')

    # 1. connection 생성
    conn = pymongo.MongoClient('localhost', 27017)
    # conn = pymongo.MongoClient(host='localhost', port=27017)
    print(conn)

    # 2. database 생성
    cloth_db = conn.my_db
    col = 'clothes' + str(url)

    # 3. collection 생성
    clothes = cloth_db[col]
    # print(clothes)

    # 4. json file open
    with open('cloth' + url + '.json', 'r', encoding='utf8') as file:
        json_data = json.load(file)
        clothes.insert_many(json_data)
    # document count
    print(clothes.estimated_document_count())

    if url == '001':
        top_total = len(cloth_total)
    elif url == '003':
        under_total = len(cloth_total)