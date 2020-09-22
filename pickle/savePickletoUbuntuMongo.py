import pickle
import pymongo

# 상의--------------------------------------------------------
with open('cloth_top.pickle', 'rb') as fr:
    cloth_top = pickle.load(fr)

conn = pymongo.MongoClient(host='localhost', port=9017, username='root', password='root',)

# 2. database 생성
my_db = 'cloth_db'
cloth_db = conn.get_database(my_db)
col = 'clothes_top'

# 3. collection 생성
clothes = cloth_db[col]

clothes.insert_many(cloth_top)

# 하의--------------------------------------------------------

with open('cloth_under.pickle', 'rb') as fr:
    cloth_under = pickle.load(fr)

conn = pymongo.MongoClient(host='localhost', port=9017, username='root', password='root',)

# 2. database 생성
my_db = 'cloth_db'
cloth_db = conn.get_database(my_db)
col = 'clothes_under'

# 3. collection 생성
clothes = cloth_db[col]
# print(clothes)

clothes.insert_many(cloth_under)

# 신발--------------------------------------------------------
with open('cloth_shoes.pickle', 'rb') as fr:
    clothes_shoes = pickle.load(fr)

conn = pymongo.MongoClient(host='localhost', port=9017, username='root', password='root',)

# 2. database 생성
my_db = 'cloth_db'
cloth_db = conn.get_database(my_db)
col = 'clothes_shoes'

# 3. collection 생성
clothes = cloth_db[col]
# print(clothes)

clothes.insert_many(clothes_shoes)