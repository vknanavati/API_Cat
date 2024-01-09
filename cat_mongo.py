import json
from pymongo import MongoClient
import requests

response = requests.get("https://api.thecatapi.com/v1/breeds", timeout=5)

data = response.content
cat_list = json.loads(data)

cluster = MongoClient("mongodb+srv://viminnanavati:sQWdsJalWw7F84Tn@cluster0.qhumshi.mongodb.net/?retryWrites=true&w=majority")

db = cluster["Cat_Breeds"]
collection = db["cat_info"]

dict_breed = " "
i = 0
for index in range(len(cat_list)):
    dict_breed = cat_list[index]
    dict_breed["_id"] = i
    i += 1
    collection.insert_one(dict_breed)

