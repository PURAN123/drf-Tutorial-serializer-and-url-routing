import requests

get_token = "http://127.0.0.1:8000/auth/"

# username = input("Enter username\n")
# password = input("Enter password\n")


creds = {
  "username" : "admin",
  "password" : "admin" 
}
token_resp = requests.post(get_token, json=creds)
if token_resp.status_code == 200:
  token = token_resp.json().get("token")
  headers =   {
    "Authorization": f"Bearer {token}",
  }
  endpoint = "http://127.0.0.1:8000/products/"
  json_data = {
    "title" :"Hello-13",
    "price": 5852
  }
  response = requests.post(endpoint, json= json_data, headers=headers);
  print(response.status_code)
  print(response)
else :
  print(token_resp.json())