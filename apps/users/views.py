from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        Ввод юзера.
        """
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)