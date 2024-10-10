import requests
from .models import Pokemon


def fetch_api_data():


    url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
    # get metode
    response = requests.get(url)
    # kad mes sutam request(jebkada metode) mes sanemam atbildi ka response, nak Json valoda.
    # lai python varetu saprast info, mums vajag partulkot json un konkreto python data type.
    # dictionary ir type.
    data = response.json()
    results = data.get("results")
    #lai mes varetu iet cauri listei un elementiem mums vajag izmantot for loop
    for pokemon in results:
        # elementi saraksta #atslega + vertiba veido dictionary
        # visur kur ir figut iekavas ir dictionary, izgustot vertiba ar .get pierakstot atslegu,
        # taja geta
        # no sava pirma objekta dabusi name, urli
        name = pokemon.get("name").capitalize()

        pokemon_details_url = pokemon.get("url")
        pokemon_detail_response = requests.get(pokemon_details_url)
        pokemon_detail_data = pokemon_detail_response.json()
        pokemon_types = pokemon_detail_data.get("types")
        pokemon_detail_type = pokemon_types[0].get("type").get("name")
        pokemon_detail_artwork = pokemon_detail_data.get("sprites").get("other").get("official-artwork").get(
            "front_default")
        pokemon_id = pokemon_detail_data.get("id")
        description_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
        pokemon_description_response = requests.get(description_url)
        pokemon_description_data = pokemon_description_response.json()
        pokemon_description = pokemon_description_data.get(
            "flavor_text_entries")[3].get("flavor_text").replace("\n", " ").replace("\u000c", " ")

        # datubaze saglaba vai atjauno objektus.
        Pokemon.objects.update_or_create(
            name=name,
            defaults={
                'url': pokemon_details_url,
                'type': pokemon_detail_type,
                'picture': pokemon_detail_artwork,
                'description': pokemon_description,

            }
        )
