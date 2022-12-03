
from rest_framework import serializers

from .models import Product




def validate_title(attrs):
    qs = Product.objects.filter(title__iexact=attrs)
    if qs.exists():
      raise serializers.ValidationError(f"{attrs} is already exists.")
    return attrs

def content_valid(attrs):
    if attrs.startswith("pass"):
        raise serializers.ValidationError(f"Content should not be empty.")
    return attrs
 