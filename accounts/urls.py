from django.urls import path, include
from .views import index, logout, login, profile, register


urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register')
]