from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from store.models import Category, Product
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from store.views import all_categories
from django.urls import reverse

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store:all_categories')  
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store:all_categories')  
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'login.html')




def logout_view(request):
    logout(request)
    login_url = reverse('accounts:login')
    return redirect(login_url)