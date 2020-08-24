import pymongo
import pandas as pd
from pymongo import MongoClient
import pandas as pd

#상의----------------------------------------------------------------------------------------
cs = pd.read_csv('../../Desktop/몽고디비저장파일/cloth_top.csv', encoding='utf-8')
top_dict = cs.to_dict("records")

# df.loc[:,['brand', 'style']]
# conn = pymongo.MongoClient('192.168.0.6', 27017)
conn = pymongo.MongoClient(host='localhost', port=27017)
print(conn)

# 2. database 생성 !!!DB바꿔야함!!!
cloth_db = conn.cloth_db
col = 'clothes_top'

# 3. collection 생성
clothes = cloth_db[col]
# print(clothes)

clothes.insert_many(top_dict)

#하의----------------------------------------------------------------------------------------
cs = pd.read_csv('../../Desktop/몽고디비저장파일/cloth_under.csv', encoding='utf-8')
under_dict = cs.to_dict("records")

# df.loc[:,['brand', 'style']]
# conn = pymongo.MongoClient('192.168.0.6', 27017)
conn = pymongo.MongoClient(host='localhost', port=27017)
print(conn)

# 2. database 생성
cloth_db = conn.cloth_db
col = 'clothes_under'

# 3. collection 생성
clothes = cloth_db[col]
# print(clothes)

clothes.insert_many(under_dict)

#신발----------------------------------------------------------------------------------------
cs = pd.read_csv('../../Desktop/몽고디비저장파일/cloth_top.csv', encoding='utf-8')
shoes_dict = cs.to_dict("records")

# df.loc[:,['brand', 'style']]
# conn = pymongo.MongoClient('192.168.0.6', 27017)
conn = pymongo.MongoClient(host='localhost', port=27017)
print(conn)

# 2. database 생성
cloth_db = conn.cloth_db
col = 'clothes_shoes'

# 3. collection 생성
clothes = cloth_db[col]
# print(clothes)

clothes.insert_many(shoes_dict)