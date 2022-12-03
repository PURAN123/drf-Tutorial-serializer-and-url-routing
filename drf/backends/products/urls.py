from django.urls import path
from .views import ProductListView, product_details_view, product_update_view, product_delete_view

urlpatterns = [
  path("", ProductListView.as_view(), name= "all_products"),
  path("<int:pk>/details/", product_details_view, name= "detail_view"),
  path("<int:pk>/update/", product_update_view, name= "update_view"),
  path("<int:pk>/delete/", product_delete_view, name= "delete_view"),
]