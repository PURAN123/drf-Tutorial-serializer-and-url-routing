
import requests

endpoint = "http://127.0.0.1:8000/products/6/"

json_data = {
  "title":"Test-1002",
  "content" :"Passfgnfjdhgjhnfgljkfm",
  "price" :1000
}

response = requests.patch(endpoint, json=json_data)

print(response.status_code)
print(response.json())

