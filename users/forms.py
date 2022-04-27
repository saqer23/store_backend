from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CreateUser(forms.ModelForm):
    username = forms.CharField(max_length=20)
    email=forms.EmailField()
    password1=forms.CharField(min_length=8,widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError('تصرف')
        return cd["password2"]
    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username = cd["username"]).exists():
            raise forms.ValidationError('تصرف مرهثانية')
        return cd["username"]
class User_UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image_profile',)