from rest_framework import generics, permissions, authentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from products.models import Product
from .serializers import ProductSerializer
from api.authentication import TokenAuth


class ProductListView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (authentication.SessionAuthentication,TokenAuth)
  filter_backends = [DjangoFilterBackend,filters.SearchFilter]
  filterset_fields = ['title', 'id']
  search_fields= ['title', "id"]

  def perform_create(self, serializer):
    title = serializer.validated_data.get("title")
    content = serializer.validated_data.get("content") or None
    if content is None:
      content = title
    serializer.save(user = self.request.user, content = content)
  
  def get_queryset(self, *args, **kwargs):
    qs=  super().get_queryset(*args, **kwargs)
    user = self.request.user;
    if(user.is_superuser):
      return qs
    elif(user.is_authenticated):
      return qs.filter(user= user)
    else :
      return Product.objects.none()



class ProductDetailView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (permissions.IsAuthenticated,)
product_details_view = ProductDetailView.as_view()



class ProductUpdateView(generics.UpdateAPIView,generics.RetrieveAPIView):
  queryset= Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes= (authentication.SessionAuthentication, TokenAuth)

  def get_queryset(self):
    qs = super().get_queryset()
    if(self.request.user.is_superuser):
      return qs
    elif self.request.user.is_authenticated:
      return qs.filter(user = self.request.user)

product_update_view = ProductUpdateView.as_view()


class ProductDeleteView(generics.DestroyAPIView, generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (permissions.IsAuthenticated,)
product_delete_view = ProductDeleteView.as_view()