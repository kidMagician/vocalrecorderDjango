# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Student(User):

    nickname= models.CharField(max_length=150,unique=True)
    REQUIRED_FIELDS = ['nickna me']
    username_validator = ASCIIUsernameValidator()


class Teacher(User):

    nickname = models.CharField(max_length=150, unique=True)
    REQUIRED_FIELDS = ['nickname']
    username_validator = ASCIIUsernameValidator()


class Lesson(models.Model):
    student = models.ForeignKey(Student, related_name='lessons',blank=True,null=True)
    teacher = models.ForeignKey(Teacher, related_name='lessons',blank=True,null=True)
    current =models.BooleanField(default=0)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    for user in Student.objects.all():
        Token.objects.get_or_create(user=user)






# Create your models here.
