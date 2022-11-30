import requests

get_token = "http://127.0.0.1:8000/auth/"

# username = input("Enter username\n")
# password = input("Enter password\n")

json_data = {
  "title" :"Hello-123",
  "price": 589
}

creds = {
  "username" : "puran",
  "password" : "password@089" 
}
token_resp = requests.post(get_token, json=creds)

if token_resp.status_code == 200:
  token = token_resp.json().get("token")
  headers =   {
    "Authorization": f"Token {token}",
  }
  endpoint = "http://127.0.0.1:8000/products/"

  response = requests.post(endpoint, json= json_data, headers=headers);
  print(response.status_code)
  print(response)