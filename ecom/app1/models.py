from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="pro_image",null=True,blank=True )
    price=models.IntegerField()
    description=models.TextField(max_length=255)
    
  
  
class Cart(models.Model):
    items = models.ManyToManyField(Products, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)