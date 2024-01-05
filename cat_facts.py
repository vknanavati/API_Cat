import requests
import json

endpoint_url = 'https://cat-fact.herokuapp.com/facts'

response = requests.get(endpoint_url)

# print(type(response))
# print(response.text)
# print(response.headers.get("Content-Type"))
# print(response.json())

data = response.content
cat_dict = json.loads(data)
# print(data_dict)
# print(cat_dict[0]["text"])
print(len(cat_dict))

for index in range(len(cat_dict)):
    print(cat_dict[index]["text"])
 
