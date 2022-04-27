from django.urls import path
from . import views

urlpatterns = [
    path('<str:store_slug>',views.store_info,name="store_info"),
]