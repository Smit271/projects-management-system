from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import UserRegisterForm, ProfilePictureForm, ProfileUpdateForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f" Account created for {username}!")
            return redirect('/user/profile')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form' : form})

@login_required
def profile(request):
    if request.method == 'POST':
        img_form = ProfilePictureForm(request.POST, request.FILES)
        context = {'img_form' : img_form }
        if img_form.is_valid():
            img_form.save(request)
            updated = True
            context = {'img_form' : img_form, 'updated' : updated }
            return render(request, 'user/profile.html', context)
        else:
            return render(request, 'user/profile.html', context)
    else:
        img_form = ProfilePictureForm()
        context = {'img_form' : img_form }
        return render(request, 'user/profile.html', context)


@login_required
def UpdateProfile(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk = id)
        print(obj)
        u_form = ProfileUpdateForm(request.POST, instance=obj)
        context = {'form': u_form}
        if u_form.is_valid():
            u_form.save()
            messages.success(request, ('Profile updated successfully'))
            return redirect(reverse('user:profile'))
        else:
            return render(request, 'user/update-profile.html', context)
    else:
        obj = User.objects.get(pk = id)
        u_form = ProfileUpdateForm(instance=obj)
        context = {
            'form': u_form,
        }
        return render(request,'user/update-profile.html', context)