from django.contrib import admin
from .models import ProdType,Products,ProdHashTag,Coment


admin.site.register(Products)
admin.site.register(ProdHashTag)
admin.site.register(ProdType)
admin.site.register(Coment)
