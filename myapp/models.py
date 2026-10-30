from django.db import models

class productModel(models.Model):
    image=models.ImageField()
    product_name=models.CharField(50)
    price=models.FloatField()
    product_description=models.TextField(max_length=500)




