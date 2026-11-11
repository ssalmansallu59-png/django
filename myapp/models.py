from django.db import models

class productModel(models.Model):
    image=models.ImageField()
    product_name=models.CharField(max_length=50)
    price=models.FloatField()
    product_description=models.TextField(max_length=500)



class registerModel(models.Model):
    fullname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    choose=[
        {"Male","Male"},
        {"Female","Female"}
    ]
    gender=models.CharField(max_length=15)
    password=models.CharField(max_length=8)
    image=models.ImageField(upload_to="profile_image",null=True)

    def __str__(self):
        return self.username



class ProductAdding(models.Model):
    image=models.ImageField(upload_to="product_image")
    product_name=models.CharField(max_length=50)
    price=models.FloatField()
    product_description=models.TextField(max_length=500)


class registrationAdding(models.Model):
    full_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    
    