# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from customAuth.models import CustomUser


def content_file_name(instance,filename):

    return '/'.join(['voice/trainingVoice', instance.vocal.student.email,instance.vocal.youtubeUrl, filename])


# class Vocal(models.Model):
#
#     youtubeUrl = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     student = models.ForeignKey(CustomUser,related_name="vocals")
#
#     def __str__(self):
#
#         return self.name


class TrainingVoice(models.Model):

    voice = models.FileField(upload_to='voice/trainingVoice')
    savedDate = models.DateTimeField()
    # vocal = models.ForeignKey(Vocal,related_name="trainginVoices")


    def __str__(self):
        return self.name







# Create your models here.
