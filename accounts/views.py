from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages


# Create your views here.

def registerUser(request): 

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'your account successfully registered')
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)

def registerVendor(request):
    return render(request, 'accounts/registerVendor.html')