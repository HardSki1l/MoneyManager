from tarfile import data_filter

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CardModel
from .serializers import *


class CardAdd(APIView):
    serializer_class = CardSerializer
    queryset = CardModel

    def post(self, request):
        card_number = request.data.get("card_number")
        card_holder = request.data("card_holder")
        money = request.data.get("money")
        CardModel.objects.create(card_number=card_number,card_holder=card_holder,money=money)
        return Response({"Message": "Karta qo`shildi"},status=201)





