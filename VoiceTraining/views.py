# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse

from .serializers import *
from customAuth.models import Teacher

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.authentication import TokenAuthentication

from django.views.decorators.csrf import csrf_exempt
from .models import Post

@authentication_classes((TokenAuthentication))
@csrf_exempt
@api_view(['POST'])
def getTrainigVoice(request):

    voiceS = TrainingVoiceSerializer(data =request.data)

    if voiceS.is_valid () :
        voiceS.validated_data['student']=request.user.student
        voiceS.save()

        return Response("good", status=status.HTTP_201_CREATED)

    else:

        return Response(status=status.HTTP_400_BAD_REQUEST)


@authentication_classes((TokenAuthentication))
@api_view(['GET'])
def searchTeacher(request):

    nickname = request.query_params.get('nickname', None)

    if nickname =="" :
        teacher = Teacher.objects.all()

    else :
        try:
            teacher = Teacher.objects.filter(nickname__contains=nickname)

        except Teacher.DoesNotExist:

            return Response("findTeacher view working well", status=status.HTTP_404_NOT_FOUND)

    teacherS = TeacherSerializer(teacher, many=True)

    return JsonResponse(teacherS.data, safe=False)


@authentication_classes((TokenAuthentication))
@api_view(['GET'])
def sendFeedback(request):

    lessons=request.user.student.lessons
    lesson =lessons.get(current=1)
    feedbacks=lesson.feedbackvoices.all()
    feedbackS=FeedBackSerializer(feedbacks,many=True)


    return Response(feedbackS.data, status=status.HTTP_200_OK)


@authentication_classes((TokenAuthentication))
@api_view(['GET'])
def post(request):

    posts = Post.objects.all()

    postSerializer = PostSerializer(posts,many=True)



    return Response(postSerializer.data,status=status.HTTP_200_OK)

@authentication_classes((TokenAuthentication))
@api_view(['POST'])
def homeworkVoiceUP(request):

    voiceS = HomeWorkVoiceSerializer(data=request.data)

    if voiceS.is_valid():
        voiceS.validated_data['student'] = request.user.student
        voiceS.save()

        return Response("good", status=status.HTTP_201_CREATED)

    else:

        return Response(status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
