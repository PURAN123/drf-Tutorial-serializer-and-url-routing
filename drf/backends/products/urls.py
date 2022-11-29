from django.urls import path
from .views import ProductListView, product_details_view

urlpatterns = [
  path("", ProductListView.as_view(), name= "all_products"),
  path("<int:pk>/", product_details_view, name= "details_view"),
]