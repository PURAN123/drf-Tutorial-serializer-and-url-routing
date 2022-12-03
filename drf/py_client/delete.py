import requests

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
    headers = {
      "Authorization": f"Bearer {token}",
    }
    endpoint = "http://127.0.0.1:8000/products/19/delete/"

    response = requests.delete(url=endpoint, headers=headers)
    print(response.status_code)
    print(response.json())