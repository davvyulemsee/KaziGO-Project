from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.urls import reverse



# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect(reverse('gigs:all_gigs'))

    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form} )


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('gigs:all_gigs'))
            else:
                form.add_error(None, "Invalid username or password.")


    else:
        form = AuthenticationForm(request=request)
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)

    return redirect(reverse('gigs:all_gigs'))
