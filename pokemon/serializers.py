from rest_framework import serializers
from .models import Pokemon, Favorite


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['pokemon', 'user_id', 'is_favorite']
        read_only_fields = ['pokemon', 'user_id']



#serializer parveido modela atributus json formata. kontrolo kuri lauki tiek izvaditi. pienemti requesta.