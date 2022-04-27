from django.urls import path
from . import views

urlpatterns = [
    path('new_product/',views.add_product,name="add_product"),
    path('<int:id>/',views.prod_detial,name="prod_detail"),
]