from django import forms
from .models import Products,ProdType,ProdHashTag,Coment


class AddProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('title','details','amount','price','img1','img2','img3','img4')

class AddComment(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ('txt',)