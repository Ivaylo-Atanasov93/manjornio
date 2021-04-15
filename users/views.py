from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from manjorno_v2.decorators import unauthenticated_user, allowed_users
# Create your views here.
from .models import Customer


@allowed_users(allowed_roles=['customer', 'delivery', 'admin'])
def user_profile_view(request):
    context = {}
    return render(request, 'user.html', context)


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def sign_up_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            Customer.objects.create(user=user, name=name, email=email)
            messages.success(request, f'Account was created for {form.cleaned_data.get("username")}')
            return redirect('login')
    context = {'form': form}
    return render(request, 'sign_up.html', context)
