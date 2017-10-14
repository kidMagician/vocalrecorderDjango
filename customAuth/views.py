# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .serializers import CUserSerializer
from .models import CustomUser

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


class JoinCUser(APIView):

    def post(self, request, format=None):

        print(request.data)
        user=CUserSerializer(data=request.data)

        if(user.is_valid()):

            print(user.validated_data)
            user.save();

            return Response("good", status=status.HTTP_201_CREATED)
        else:
            print("notgood")
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # queryset = CustomUser.objects.all()
    # serializer_class = CUserSerializer






# Create your views here.
