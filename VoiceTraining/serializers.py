from customAuth.models import Teacher
from rest_framework import serializers
from datetime import datetime
from .models import TrainingVoice,HomeWorkVoice


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('nickname',)


class TrainingVoiceSerializer(serializers.Serializer):

    savedDate = serializers.IntegerField()
    length = serializers.IntegerField()
    voiceFile = serializers.FileField()
    youtube_id = serializers.CharField()

    def create(self, validated_data):

        student = validated_data['student']
        lesson = student.lessons.get(current=1)

        voice = TrainingVoice.objects.create(voiceFile=validated_data['voiceFile'],
                              length=validated_data['length'],
                              lesson=lesson,
                              savedDate=datetime.fromtimestamp(validated_data['savedDate']//1000.0))

        return voice

class FeedBackSerializer(serializers.Serializer):

    voiceFile = serializers.FileField()
    savedDate = serializers.DateTimeField()
    subject = serializers.CharField()


class PostSerializer(serializers.Serializer):

    title = serializers.CharField()
    content = serializers.CharField()
    author = serializers.CharField()
    published_date = serializers.DateTimeField()

class HomeWorkVoiceSerializer(serializers.Serializer):

    voiceFile = serializers.FileField()
    savedDate = serializers.IntegerField()

    def create(self, validated_data):

        student = validated_data['student']
        lesson = student.lessons.get(current=1)

        voice = HomeWorkVoice.objects.create(voiceFile=validated_data['voiceFile'],
                              lesson=lesson,
                              savedDate=datetime.fromtimestamp(validated_data['savedDate']//1000.0))

        return voice