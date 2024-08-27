from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import HistoryModel
from CardApp.models import CardModel
from drf_yasg.utils import swagger_auto_schema


class HistoryAdd(APIView):
    serializer_class = HistoryModelSerializer
    queryset = HistoryModel

    @swagger_auto_schema(request_body=HistoryModelSerializer)
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


import datetime


class DayHistory(APIView):

    def get(self, request):
        day = datetime.datetime.now()
        day = day.strftime("%d")
        filtr1 = HistoryModel.objects.filter(when_date__day=26)
        for i in filtr1:
            print(i.when_date)
        return Response({'msg': "ok"})


class MonthHistory(APIView):
    def get(self, request):
        month = datetime.datetime.now()
        month = month.strftime("%m")
        print(month)
        filtr2 = HistoryModel.objects.filter(when_date__month=month)
        all_data = {}
        for i in filtr2:
            all_data[i.who_payed.username] = [i.when_date, i.card_related.card_number, i.where]
        return Response(all_data, status=200)


class TopDayPayed(APIView):
    def get(self, request):
        day = datetime.datetime.now().day
        try:
            filtr1 = HistoryModel.objects.filter(when_date__day=day).order_by('-price').first()
            if filtr1:
                serializer = HistoryModelSerializer1(filtr1)
                return Response(serializer.data, status=200)
            else:
                return Response({"detail": "No data found for today"}, status=404)
        except HistoryModel.DoesNotExist:
            return Response({"detail": "No data found for today"}, status=404)

        # return Response(serializer.data, status=200)
