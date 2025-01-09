from django.shortcuts import render, redirect, get_object_or_404
from .models import Pokemon
from users.models import FavoritePokemon
from django.contrib import messages


def add_favorite_pokemon(request, pokemon_name):
    # ta tu vari dabut useri kas ir ielagojies sesija
    user = request.user
    # mes pasaucam FavoritePokemon modeli
    pokemon = get_object_or_404(Pokemon, name=pokemon_name)

    favorite_pokemon, created = FavoritePokemon.objects.get_or_create(
        pokemon=pokemon,
        user=user,
    )
    if created:
        messages.success(request, f'{pokemon_name} Pokemon was added to your favorites')
    else:
        messages.warning(request, f' {pokemon_name} already exists')

    # taisnais direct pec informacijas aptrades pasviez uz vajadzigo lapu
    return redirect('favorites')


def favorite_pokemons_list(request):
    user = request.user
    favorite_pokemons = FavoritePokemon.objects.filter(user=user)

    context = {
        'favorites': favorite_pokemons
    }

    return render(request, 'users/favorites.html', context)
