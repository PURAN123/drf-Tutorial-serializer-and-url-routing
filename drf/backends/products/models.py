from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=120)
    content  = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,default=59.58)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)