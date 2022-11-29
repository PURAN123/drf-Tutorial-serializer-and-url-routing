from django.urls import path

from .views import home_page, all_products
urlpatterns = [
  path("", home_page, name = "home_page"),
  path("product/", all_products, name= "all_products"),
]
