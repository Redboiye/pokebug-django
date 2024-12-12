from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
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
