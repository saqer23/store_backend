from django.shortcuts import render
from .models import StoreInfo


def store_info(request,store_slug):
    s = StoreInfo.objects.get(store_slug=store_slug)
    context = {
        'Store':s,
    }
    return render(request,'mystore/create_store.html',context)

