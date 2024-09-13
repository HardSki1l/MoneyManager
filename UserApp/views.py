from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from .autorization import CustomJWTAuthentication


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


class Login(APIView):
    @swagger_auto_schema(request_body=UserLoginSRl)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = UsersInfoModel.objects.all().filter(username=username, password=password).first()
        serializer = UserRegisterSRL(user)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }, status=200)
        else:
            return Response({"message": "User Topilmadi"})


class TestJWT(APIView):
    authentication_classes = (CustomJWTAuthentication,)

    def get(self, request):
        return Response("Worked JWT Token", 200)
