import requests
from django.shortcuts import render, get_object_or_404
from .models import Pokemon


# request ir metadati, url, sakara ar backend komunikaciju
def home(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
    response = requests.get(url)
    data = response.json()
    results = data.get("results")

    for pokemon in results:
        name = pokemon.get("name").capitalize()
        pokemon_details_url = pokemon.get("url")
        pokemon_detail_response = requests.get(pokemon_details_url)
        pokemon_detail_data = pokemon_detail_response.json()
        pokemon_types = pokemon_detail_data.get("types")
        print(pokemon_types)


        Pokemon.objects.update_or_create(
            name=name, url=pokemon_details_url,

        )

    # ORM metode all pasauc objektus no Pokemon
    pokemons = Pokemon.objects.all()
    # context pado informaciju uz html un ir pieejama ar conteksta atslegam
    context = {"all_pokemons": pokemons}

    return render(request, "pokemon/index.html", context)


def pokemon_detail(request, pokemon_id, ):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    context = {"pokemon": pokemon, "type": pokemon.type.lower()}

    return render(request, "pokemon/pokemon_details.html", context)
