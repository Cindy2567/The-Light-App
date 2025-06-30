from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import logout



# Register view
def register(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('home')  # Redirect to home after registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


# Login view
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'registration/login.html')



# Optional: Protected home view
@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

