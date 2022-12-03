from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title
from api.serializers import UserSerializer


class ProductInlineSerializer(serializers.Serializer):
  title = serializers.CharField(read_only=True)
  url = serializers.HyperlinkedIdentityField(view_name='detail_view', lookup_field='pk',read_only=True)



class ProductSerializer(serializers.ModelSerializer) :
  owner = UserSerializer(source='user',read_only=True)
  # related_products = ProductInlineSerializer(source= 'user.product_set.all', read_only=True, many=True)
  discount = serializers.SerializerMethodField(read_only=True)
  edit_url = serializers.SerializerMethodField(read_only=True)
  url = serializers.HyperlinkedIdentityField(view_name='detail_view', lookup_field='pk')
  delete_url = serializers.HyperlinkedIdentityField(view_name='delete_view', lookup_field='pk')
  title = serializers.CharField(validators= [validate_title])
  #email = serializers.EmailField(write_only=True)
  class Meta:
    model = Product
    fields = [
      "id",
      'owner',
      'url',
      "edit_url",
      "delete_url",
      "title",
      "content",
      "price",
      "sale_price",
      "discount",
      #'related_products'
    ]


  def get_edit_url(self, obj):
    request = self.context.get('request')
    if request is None:
      return None
    return reverse("update_view", kwargs={'pk':obj.id},request= request )

  def get_discount(self, obj):
    if not hasattr(obj, "id"):
      return None
    return obj.get_discount()

  # def validate_title(self, attrs):
  #   qs = Product.objects.filter(title__iexact=attrs)
  #   if qs.exists():

  #     raise serializers.ValidationError(f"{attrs} is already exists.")
  #   return attrs

  # def create(self, validated_data):
  #   # email = validated_data.pop('email')
  #   # print(email)
  #   return super().create(validated_data)

  # def update(self, instance, validated_data):
  #   instance.title = validated_data['title']
  #   print( validated_data['title'])
  #   return super().update(instance, validated_data)