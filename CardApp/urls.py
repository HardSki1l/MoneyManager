from django.urls import path
from .views import *

urlpatterns = [
    path('add/', CardAdd.as_view())
]
