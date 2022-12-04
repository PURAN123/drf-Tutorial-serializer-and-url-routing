from rest_framework.authentication import TokenAuthentication as BaseAuth

class TokenAuth(BaseAuth):
    keyword = 'Token'