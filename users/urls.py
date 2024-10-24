from django.urls import path
from .views import register, user_login, log_out, favorite_pokemons_list, add_favorite_pokemon

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', log_out, name='logout'),
    path('favorites/', favorite_pokemons_list, name='favorites'),
    path('add_favorite_pokemons/<str:pokemon_name>', add_favorite_pokemon, name='add_favorite_pokemons'),
]
