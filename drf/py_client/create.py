import requests



endpoint = "http://127.0.0.1:8000/products/"

json_data = {
  "title" :"Hello-6",
  "price": 558
}

response = requests.post(endpoint, json= json_data);
print(response.status_code)
print(response)