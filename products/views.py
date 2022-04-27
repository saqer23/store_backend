from django.shortcuts import render,redirect
from .forms import AddProduct,AddComment
from .models import Products,Coment

def add_product(request):
    user = request.user
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            new_prod = form.save(commit=False)
            new_prod.user = user
            new_prod.save()
            return redirect('home')
    else:
        form = AddProduct()
    context = {
        'form':form,
    }
    return render(request,'products/add_product.html',context)


def prod_detial(request,id):
    prod = Products.objects.get(id=id)
    comment = prod.comments.filter(active=True)
    user =request.user
    if request.method == "POST":
        commint_form = AddComment(request.POST)
        if commint_form.is_valid():
            new_commeint = commint_form.save(commit=False)
            new_commeint.user = user
            new_commeint.prod = prod
            new_commeint.save()
            return redirect('home')
    else:
        commint_form = AddComment()
    context = {
        'prod':prod,
        'commint_form':commint_form,
        'comment':comment,
    }
    return render(request,'products/product_details.html',context)