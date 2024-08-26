from django.urls import path
from .views import HistoryAdd,DayHistory

urlpatterns = [
    path('add/', HistoryAdd.as_view()),
    path('day/',DayHistory.as_view())
]
