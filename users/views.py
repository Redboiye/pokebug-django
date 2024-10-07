from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", context={"form": form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=user_name, password=password)
            # ja pareizi tad atgriezis user objektu
            if user:
                login(request, user)
                # ar tuksu formu parmet atpakal uz login, ka tiesibas ir redzet non-register useriem.
                return redirect('home')
                # pedejais if pariet uz else funkciju

            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", context={"form": form})


def log_out(request):
    logout(request)
    return redirect('home')
