from django.contrib import admin
from .models import Phone, Purchase

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('model', 'price')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('phone', 'buyer_name', 'buyer_phone', 'purchase_date')
