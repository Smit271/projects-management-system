from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import UserRegisterForm, ProfilePictureForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
        print('PRINT 1: ', img_form)
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
