from .api import fetch_api_data
from django.shortcuts import render, get_object_or_404
from .models import Pokemon



# request ir metadati, url, sakara ar backend komunikaciju
def home(request):
    # ORM metode all pasauc objektus no Pokemon
    pokemons = Pokemon.objects.all()
    # ja pokemonu datubazu ir nulle elementu, tad mes vinus ieladejam no api
    if len(pokemons) < 1:
        fetch_api_data()
        # kapec nav vajadzigs mainigais, nav return, jo nevajag neko atgriest, backgrounda viss ir!

    # context pado informaciju uz html un ir pieejama ar conteksta atslegam
    context = {"all_pokemons": pokemons}

    return render(request, "pokemon/index.html", context)


def pokemon_detail(request, pokemon_name):
    pokemon = get_object_or_404(Pokemon, name=pokemon_name)
    context = {"pokemon": pokemon, "type": pokemon.type.lower()}

    return render(request, "pokemon/pokemon_details.html", context)



