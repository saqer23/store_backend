from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic


from .forms import CreateUser , User_UpdateForm,ProfilUpdateForm
from django.views.generic import DetailView
def register(request):
    if request.method == 'POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            #username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            return redirect('home')
    else:
        form = CreateUser()

    context = {
        'form':form,
    }
    return render(request,'users/register.html',context)
def home(request):
    return render(request,'users/home.html')
def profile(request):
    user=request.user
    context={
        'user':user,
    }
    return render(request,'users/profile.html')

def profile_update(request):
    user_form = User_UpdateForm(request.POST, instance=request.user)
    profile_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    if request.method == 'POST':
        user_form = User_UpdateForm(request.POST, instance=request.user)
        profile_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            update_user = user_form.save(commit=False)
            update_user.set_password(user_form.cleaned_data['password2'])
            update_user.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = User_UpdateForm(instance=request.user)
        profile_form = ProfilUpdateForm(instance=request.user.profile)

    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/profile_update.html', context)



def userDeleteView(request,pk):
    uname=User.objects.get(pk=pk)
    b=User.objects.filter(username=uname.username)
    b.delete()
    uname.delete()
    return redirect('home')

def SetUserImageDefault(self):
    self.user.profile.image_profile.delete(save=False)  # delete old image file
    self.user.profile.image_profile = 'folder.jpg' # set default image
    self.user.profile.save()
    return redirect('home')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm()
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user
