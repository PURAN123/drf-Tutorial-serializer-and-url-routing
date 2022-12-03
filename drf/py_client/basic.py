import requests

endpoint = "http://127.0.0.1:8000/product/"


response = requests.get(endpoint,json={"query":"hello World"})
# print(response.headers)
# print(response.text)

print(response.json())
