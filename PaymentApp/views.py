from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import HistoryModel
from CardApp.models import CardModel

class HistoryAdd(APIView):
    serializer_class = HistoryModelSerializer
    queryset = HistoryModel

    def post(self, request):
        card_related = request.data.get("card_related")
        price = request.data.get("price")
        where = request.data.get("where")
        card_instance = CardModel.objects.get(id=card_related)
        HistoryModel.objects.create(card_related=card_instance, price=price, where=where)
        return Response({"Message": "History yaratildi"}, status=200)

