from django.db import models
from django.contrib.auth.models import User

class StoreType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

class StoreInfo(models.Model):
    store_name = models.CharField(max_length=50)
    store_type = models.ForeignKey(StoreType,on_delete=models.CASCADE)
    store_owner = models.OneToOneField(User,on_delete=models.CASCADE)
    business_account = models.ImageField(blank=True,null=True,upload_to='business_account')
    store_slug = models.SlugField(max_length=15)

    def __str__(self):
        return self.store_name


class SubscribeType(models.Model):
    subscribe_type = models.CharField(max_length=20)

    def __str__(self):
        return self.subscribe_type


class SubscribeStore(models.Model):
    subscribetype = models.ForeignKey(SubscribeType,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bay_img = models.ImageField(upload_to='bay_image')
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.active)