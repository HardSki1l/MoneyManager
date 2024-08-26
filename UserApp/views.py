from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from django.shortcuts import render
from .serializers import *
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class UserRegisterView(APIView):

    serializer_class = UserRegisterSRL
    @swagger_auto_schema(request_body=UserRegisterSRL)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors)
