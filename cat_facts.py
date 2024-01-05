import requests
import json
import random

endpoint_url = 'https://cat-fact.herokuapp.com/facts'

response = requests.get(endpoint_url)

type(response)
# response.text
response.headers.get("Content-Type")
response.json()

data = response.content
cat_dict = json.loads(data)

rand_index = random.randint(0,len(cat_dict)-1)
print(cat_dict[rand_index]["text"])

 
