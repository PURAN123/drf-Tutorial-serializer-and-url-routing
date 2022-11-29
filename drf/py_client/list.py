import requests

endpoint = "http://127.0.0.1:8000/products/"

response = requests.get(endpoint);
print(response.status_code)
print(response.json())