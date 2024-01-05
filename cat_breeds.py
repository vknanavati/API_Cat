import requests
import json

response = requests.get("https://api.thecatapi.com/v1/breeds")

data = response.content
#cat_list is a list of dictionaries for each breed
cat_list = json.loads(data)

#retrieve name each key
print(cat_list[0].keys())
