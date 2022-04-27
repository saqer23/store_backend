from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name="register"),
    path('home/',views.home,name="home"),
    path('login/',LoginView.as_view(template_name='users/Login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='users/Logout.html'), name='logout'),
    path('profile/', views.profile, name="profile"),
    path('profile_update/', views.profile_update, name="profile_update"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)