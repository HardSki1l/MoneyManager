from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import HistoryModel
from CardApp.models import CardModel

class HistoryAdd(APIView):
    serializer_class = HistoryModelSerializer
    queryset = HistoryModel

    def post(self, request):
        card_related = int(request.data.get("card_related"))
        price = request.data.get("price")
        where = request.data.get("where")
        filtr_1 = CardModel.objects.filter(id=card_related).first()
        HistoryModel.objects.create(card_related=card_related, price=price, where=where)
        return Response({"Message": "History yaratildi"}, status=200)

class HistoryAdd1(APIView):
    serializer_class = HistoryModelSerializer
    queryset = HistoryModel

    def post(self, request):
        serializer = HistoryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "History yaratildi"}, status=201)
        else:
            return Response(serializer.errors)




