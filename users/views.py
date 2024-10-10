from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import Pokemon
from users.models import FavoritePokemon


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


def add_favorite_pokemon(request, pokemon_name):
    pokemon = get_object_or_404(Pokemon, name=pokemon_name)
    # ta tu vari dabut useri kas ir ielagojies sesija
    user = request.user
    #mes pasaucam FavoritePokemon modeli
    FavoritePokemon.objects.create(user=user, pokemon=pokemon)
        #taisnais direct pec informacijas aptrades pasviez uz vajadzigo lapu
    return redirect('pokemon_detail', pokemon_name=pokemon_name)


def favorite_pokemons_list(request):
    user = request.user
    favorite_pokemons = FavoritePokemon.objects.filter(user=user)

    context = {
        'favorites': favorite_pokemons
    }

    return render(request, 'users/favorites.html', context)
