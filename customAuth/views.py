# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .serializers import CUserSerializer, FIndPassSerializer,LessonSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class JoinCUser(APIView):

    def post(self, request, format=None):

        userS=CUserSerializer(data=request.data)
        lessonS =LessonSerializer(data=request.data)

        if userS.is_valid() and lessonS.is_valid():

            try:
                validate_email(userS.validated_data['username'])
                userS.save()
                lessonS.save()

                return Response("good",status=status.HTTP_201_CREATED)

            except ValidationError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class FIndPass(APIView):

    def post(self,request,format=None):

        findPassdata =FIndPassSerializer(data=request.data)

        if findPassdata.is_valid():

            try:
                validate_email(findPassdata.validated_data['username'])

                print("working")
                # send email

                return Response(status=status.HTTP_200_OK)

            except validate_email.ValidationError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
