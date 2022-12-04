import requests
# from getpass import getpass
# username = input("Enter username\n")
# password = input("Enter password\n")

get_token = "http://127.0.0.1:8000/auth/"

creds = {
  "username" : "puran",
  "password" : "password@089" 
}
# creds = {
#   "username" : "admin",
#   "password" : "admin" 
# }
token_resp = requests.post(get_token, json=creds)

if(token_resp.status_code == 200):
    token = token_resp.json().get('token')
    headers =   {
      "Authorization": f"Token {token}",
    }
    endpoint = "http://localhost:8000/products/23/update/"
    json_data = {
      "title" : "Hello-1-test123",
    }
    response = requests.patch(endpoint, json=json_data, headers=headers)
    print(response.status_code)
    print(response.json())


