from rest_framework import serializers
from .models import Student,Lesson,Teacher
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _


class CUserSerializer(serializers.Serializer):

    username = serializers.CharField()
    nickname = serializers.CharField()
    password = serializers.CharField()


    def create(self, validated_data):

        return Student.objects.create_user(**validated_data)

    def update(self, instance, validated_data):

        user = Student.objects.get(email = validated_data.email)
        user.set_password(validated_data.password1)


class LessonSerializer(serializers.Serializer):

    nickname = serializers.CharField()
    teacher_nick =serializers.CharField()

    def create(self, validated_data):

       return Lesson.objects.create(student=Student.objects.get(nickname=validated_data['nickname']),
                              teacher=Teacher.objects.get(nickname=validated_data['teacher_nick']),current=True)


class FIndPassSerializer(serializers.Serializer):

    username = serializers.CharField()

