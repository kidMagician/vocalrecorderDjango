# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from customAuth.models import Lesson,Teacher


def content_file_name(instance,filename):

    return '/'.join(['voice/trainingVoice', instance.vocal.student.email,instance.vocal.youtubeUrl, filename])


class FeedBackVoice(models.Model):

    voiceFile = models.FileField(upload_to='voice/trainingVoice')
    savedDate = models.DateTimeField()
    subject = models.CharField(max_length=100, default="initialize")
    lesson = models.ForeignKey(Lesson, related_name="feedbackvoices")

    def __str__(self):
        return self.subject


class HomeWorkVoice(models.Model):

    voiceFile = models.FileField(upload_to='voice/trainingVoice')
    savedDate = models.DateTimeField()
    lesson = models.ForeignKey(Lesson, related_name="homeworkVoices")


class TrainingVoice(models.Model):

    voiceFile = models.FileField(upload_to='voice/trainingVoice')
    savedDate = models.DateTimeField()
    length= models.IntegerField(null =True)
    evaluation = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, related_name="lessons", null=True)
    youtube_id = models.CharField(max_length=100, null=True)


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author= models.CharField(max_length=100)
    published_date = models.DateTimeField()



# Create your models here.
