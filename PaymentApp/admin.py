from django.contrib import admin
from .models import HistoryModel


# Register your models here.

class SearchHistoryModel(admin.ModelAdmin):
    list_display = ['card_related', 'who_payed', 'price', 'when_date', 'where']


admin.site.register(HistoryModel,SearchHistoryModel)
