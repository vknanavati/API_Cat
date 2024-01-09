import json
import os
from pymongo import MongoClient
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://vknanavati:{password}@cluster0.qhumshi.mongodb.net/?retryWrites=true&w=majority"
cluster = MongoClient(connection_string)

response = requests.get("https://api.thecatapi.com/v1/breeds", timeout=5)

data = response.content
cat_list = json.loads(data)


db = cluster["Cat_Breeds"]
collection = db["cat_info"]

# delete keys from each dictionary
collection.update_many({}, {"$unset":{"cfa_url":1}})
collection.update_many({}, {"$unset":{"vetstreet_url":1}})
collection.update_many({}, {"$unset":{"vcahospitals_url":1}})
collection.update_many({}, {"$unset":{"country_codes":1}})
collection.update_many({}, {"$unset":{"country_code":1}})
collection.update_many({}, {"$unset":{"wikipedia_url":1}})
collection.update_many({}, {"$unset":{"reference_image_id":1}})
collection.update_many({}, {"$unset":{"alt_names":1}})
