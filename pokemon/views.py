from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PokemonSerializer
from .models import Pokemon, Favorite


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


class LogInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:

            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return Response({"message": "Login SuccessesFully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f'{e}'}, status=401)


class LogOutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout Successful"}, status=status.HTTP_201_CREATED)

def add_favorite(request, pokemon_id):
    user_id = request.GET.get("user_id")
    if not user_id:
        return JsonResponse({"error": "User ID is required"}, status=400)

    try:
        if request.method == "POST":
            pokemon = Pokemon.objects.get(id=pokemon_id)
            favorite, created = Favorite.objects.get_or_create(pokemon=pokemon, user_id=user_id)
            favorite.is_favorite = not favorite.is_favorite
            favorite.save()
            return JsonResponse({"pokemon": pokemon.name, "is_favorite": favorite.is_favorite})
    except Pokemon.DoesNotExist:
        return JsonResponse({"error": "Pokemon not found"}, status=404)