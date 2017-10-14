# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView

from .froms import TrainingVoiceForm

from django.utils import timezone

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
def post_new(request):

    print("good")

    if request.method == "POST":

        voiceForm = TrainingVoiceForm(request.POST,request.FILES)
        print(request.POST)
        print(voiceForm)
        print("good2")

        if voiceForm.is_valid():

            print("good3")

            voice=voiceForm.save(commit=False)
            voice.savedDate = timezone.now()
            voice.save()

            return Response("good", status=status.HTTP_201_CREATED)

        else:
            print("not good")

            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        form = TrainingVoiceForm()
        return render(request, 'voiceTest.html', {'form': form})

# Create your views here.
