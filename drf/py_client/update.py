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
      "Authorization": f"Bearer {str(token)}",
    }
    endpoint = "http://localhost:8000/products/1/update/"
    json_data = {
      "title" : "Hello-1-525523",
      "content":"content-1 found",
      "price" : 150
    }
    response = requests.put(endpoint, json=json_data, headers=headers)
    print(response.status_code)
    print(response.json())


