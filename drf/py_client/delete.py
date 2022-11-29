import requests


endpoint = "http://127.0.0.1:8000/products/5/"

response = requests.delete(url=endpoint)


print(response)