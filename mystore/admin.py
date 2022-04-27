from django.contrib import admin
from .models import StoreType,StoreInfo,SubscribeType,SubscribeStore



admin.site.register(StoreType)
admin.site.register(StoreInfo)
admin.site.register(SubscribeType)
admin.site.register(SubscribeStore)