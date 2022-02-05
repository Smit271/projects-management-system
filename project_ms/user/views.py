from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.

def login(request):
    return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            user = form.save()
            created = True
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {'created' : created}
            return render(request, 'user/register.html', context)
        else:
            return render(request, 'user/register.html', context)
    else:
        form = UserRegisterForm()
        context = {
            'form' : form,
        }
        return render(request, 'user/register.html', context)