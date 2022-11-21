import requests

endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint,json={"query":"hello World"})

print(response.text)