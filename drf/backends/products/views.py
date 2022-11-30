

from rest_framework import generics, permissions, authentication
from products.models import Product
from .serializers import ProductSerializer


class ProductListView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (authentication.TokenAuthentication,authentication.SessionAuthentication)

  def perform_create(self, serializer):
    title = serializer.validated_data.get("title")
    content = serializer.validated_data.get("content") or None
    if content is None:
      content = title
    serializer.save(content= content)


class ProductDetailView(generics.RetrieveAPIView,generics.UpdateAPIView, generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (permissions.IsAuthenticated,)

product_details_view = ProductDetailView.as_view()