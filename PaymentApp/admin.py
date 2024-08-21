from django.contrib import admin
from .models import HistoryModel

class SearchHistoryModel(admin.ModelAdmin):
    exclude = ('who_payed',)
    list_display = ['card_related', 'who_payed', 'price', 'when_date', 'where']


admin.site.register(HistoryModel,SearchHistoryModel)
