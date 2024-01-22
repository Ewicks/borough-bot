from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('1')
            login(request, user)
            print('2')
            return redirect('test')
        else:
            messages.success(request, ('There was an error logging in '))
            return redirect('login')
            
    else:
        return render(request, 'authenticate/login.html', {})


def register_user(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, ('successfully signed in'))
            login(request, user)
            return redirect('test')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {'form': form})