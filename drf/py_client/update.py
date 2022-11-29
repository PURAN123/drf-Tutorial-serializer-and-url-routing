import requests


endpoint = "http://127.0.0.1:8000/products/7/"

json_data = {
  "title" : "Hello-100234",
  "content":"passs"
}

response = requests.put(endpoint, json=json_data)

print(response.status_code)
print(response.json())


