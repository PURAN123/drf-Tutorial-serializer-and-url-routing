import json

from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer



@api_view(["GET"])
def all_products(request):
  queryset = Product.objects.all()
  serializer = ProductSerializer(queryset, many= True,context={'request':request})
  return Response(serializer.data)  


@api_view(["GET"])
def home_page(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data = ProductSerializer(model_data).data
        data = model_to_dict(model_data, fields=[ "id", "title",  "price", 'user',])
        # json_data = dict(data)
        # json_data = json.dumps(data)
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
    return Response(data)





# def home_page(request, *args, **kwargs):
#   body = request.body # body is json parameter in django
#   data = {}
#   try:
#     data = json.loads(body) # convert byte string to python dictionary
#   except :
#     pass
#   data["content_type"] = request.content_type
#   data['headers'] = dict(request.headers)
#   data['params'] = dict(request.GET) # GET is query parameter
#   return JsonResponse(data)


