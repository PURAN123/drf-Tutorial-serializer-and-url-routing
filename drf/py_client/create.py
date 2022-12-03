import requests

# from getpass import getpass
# username = input("Enter username\n")
# password = input("Enter password\n")

get_token = "http://127.0.0.1:8000/auth/"

creds = {
  "username" : "puran",
  "password" : "password@089" 
}
token_resp = requests.post(get_token, json=creds)

if token_resp.status_code == 200:
  token = token_resp.json().get("token")
  headers =   {
    "Authorization": f"Bearer {token}",
  }
  endpoint = "http://127.0.0.1:8000/products/"
  json_data = {
    "title" :"Hello-27",
    "price": 5852,
    "content":"Hello item 27 here"
  }
  response = requests.post(endpoint, json= json_data, headers=headers);
  print(response.status_code)
  print(response)
else :
  print(token_resp.json())