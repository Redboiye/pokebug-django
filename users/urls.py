from django.urls import path
from .views import add_favorite_pokemon, favorite_pokemons_list

urlpatterns = [

    path('favorites/', favorite_pokemons_list, name='favorites'),
    path('add_favorite_pokemons/<str:pokemon_name>', add_favorite_pokemon, name='add_favorite_pokemons'),
]
