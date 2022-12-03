from django.db import models

from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    content  = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,default=59.58)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "%.2f" %(float(self.sale_price) * 0.1)
    # def get_discount(self):
    #     return "122"