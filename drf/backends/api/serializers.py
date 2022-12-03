
from rest_framework import serializers


class UserProductSerializer(serializers.Serializer):
  title = serializers.CharField(read_only=True)
  url = serializers.HyperlinkedIdentityField(view_name='detail_view', lookup_field='pk',read_only=True)



class UserSerializer(serializers.Serializer):
  id= serializers.UUIDField(read_only=True)
  username = serializers.CharField(read_only=True);
  other_products = serializers.SerializerMethodField(read_only=True)

  def get_other_products(self, obj):
    user = obj
    my_products_qs = user.product_set.all()[:1]
    return UserProductSerializer(my_products_qs, many=True, context = self.context).data
