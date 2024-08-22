from django.urls import path
from .views import HistoryAdd

urlpatterns = [
    path('add/', HistoryAdd.as_view())
]
