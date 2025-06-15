from django.urls import path
from .views import register, login, home

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('', home, name='home'),
]