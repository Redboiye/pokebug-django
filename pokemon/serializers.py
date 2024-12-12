from rest_framework import serializers
from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


#serializer parveido modela atributus json formata. kontrolo kuri lauki tiek izvaditi. pienemti requesta.