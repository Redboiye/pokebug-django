from django.shortcuts import render, get_object_or_404
from .models import Pokemon


# request ir metadati, url, sakara ar backend komunikaciju
def home(request):
    # ORM metode all pasauc objektus no Pokemon
    pokemons = Pokemon.objects.all()
    # context pado informaciju uz html un ir pieejama ar conteksta atslegam
    context = {"all_pokemons": pokemons}

    return render(request, "pokemon/index.html", context)


def pokemon_detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    context = {"pokemon": pokemon}

    return render(request, "pokemon/pokemon_details.html", context)
