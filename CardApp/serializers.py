from .models import CardModel
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = ('card_number', 'card_holder', 'money')
