from django.contrib import admin
from django.urls import path, include

from UserApp.views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view())
]
