from django.urls import path
from .views import register, user_login, log_out


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', log_out, name='logout'),
]
