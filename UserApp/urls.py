from django.contrib import admin
from django.urls import path, include

from UserApp.views import UserRegisterView, Login, TestJWT

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/',Login.as_view()),
    path('testjwt/',TestJWT.as_view())
]
