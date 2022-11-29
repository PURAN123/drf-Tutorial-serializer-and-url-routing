from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display=  ("title", "content", "price", "sale_price")

