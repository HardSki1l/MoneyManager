from django.urls import path
from .views import HistoryAdd, DayHistory, MonthHistory,TopDayPayed

urlpatterns = [
    path('add/', HistoryAdd.as_view()),
    path('day/',DayHistory.as_view()),
    path('month/', MonthHistory.as_view()),
    path('top/day',TopDayPayed.as_view())

]
