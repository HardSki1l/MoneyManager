from .models import HistoryModel
from rest_framework import serializers


class HistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModel
        fields = ("card_related", "price", "where")
