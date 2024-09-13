from rest_framework import serializers
from .models import *


class UserRegisterSRL(serializers.ModelSerializer):
    class Meta:
        model = UsersInfoModel

        fields = '__all__'


class UserLoginSRl(serializers.ModelSerializer):
    class Meta:
        model = UsersInfoModel
        fields = ("username", "password",)
