
from rest_framework import viewsets
from .serializers import PokemonSerializer
from .models import Pokemon


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = []

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name=name)
        return queryset



