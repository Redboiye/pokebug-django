from django.db import models
from pokemon.models import Pokemon
from django.contrib.auth.models import User


# butiba favorite, savam uzeram saglaba milakos pokemonus, ikona kas saglaba ka favorite

# izveido modeli favorite pokemon, kas sevi ietvers divus atributus, user ka foreign key, un pokemon ka foreign key
# ka varam dabut tos pokemonus, favorite_pokemon.modela nosaukums, Favorite pokemon.object.filter
# saglabat, ar postu no html, nosutot no pokemona detalam, objekta id un usera id
# tad abus divus foreign key saglabas ieks favorite pokemon
# jauns view kas bus favorite, un ielikt to navigation bara
# favorite viewa dabusi ara visus tos pokemonus pec favorite.objects.filter
# visu taisit pokemona viewa

class FavoritePokemon(models.Model):
    # sis modelis paradis un saglaba useri un favorite pokemon, user+favorite kombinacijas, saglabas datubaze
    # mes lietojama on_delete prieks ForeignKeys. Set_null butu undefined, ar CASCADE tu pilniba izdzess.
    #set_null izmanto prieks scoringa
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,

        on_delete=models.CASCADE,
    )
    pokemon = models.ForeignKey(
        Pokemon,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user
