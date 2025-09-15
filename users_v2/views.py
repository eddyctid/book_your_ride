from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["mobile_num","email", "is_superuser", "is_staff","is_active","last_login"]

# Create your views here.
class UserListView(ListAPIView):
    serializer_class = UserModelSerializer
    queryset = get_user_model().objects.all()