from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .api import fetch_api_data
from .serializers import PokemonSerializer,FavoriteSerializer
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


class LogInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return Response({"message": "Login SuccessesFully", "user": user.id},
                                status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f'{e}'}, status=401)


class LogOutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout Successful"}, status=status.HTTP_201_CREATED)


class AddFavorite(APIView):
    permission_classes = []

    def post(self, request, pokemon_id):
        pokemon = Pokemon.objects.get(pk=pokemon_id)
        user_name = request.data.get("user_id")
        user = User.objects.get(username=user_name).id
        data = {"pokemon": pokemon.id, "user_id": user}
        serializer = FavoriteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
