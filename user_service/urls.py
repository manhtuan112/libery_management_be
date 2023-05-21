from django.urls import path
from user_service.views import UserLogin, UserRegister
urlpatterns = [
    path('register/',UserRegister, name="register"),
    path('login/', UserLogin, name="login"),

]