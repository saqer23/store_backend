from django.db import models
from django.contrib.auth.models import User


class ProdType(models.Model):
    product_type = models.CharField(max_length=30)

    def __str__(self):
        return self.product_type


class Products(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    details = models.TextField()
    amount = models.IntegerField()
    price = models.FloatField()
    img1 = models.ImageField(default="bank.PNG",upload_to='products')
    img2 = models.ImageField(blank=True,null=True)
    img3 = models.ImageField(blank=True, null=True)
    img4 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class ProdHashTag(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    hastag = models.ForeignKey(ProdType,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title



class Coment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    txt = models.TextField()
    prod = models.ForeignKey(Products,on_delete=models.CASCADE,related_name="comments")
    active = models.BooleanField(default=False)