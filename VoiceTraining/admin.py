# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


@admin.register(TrainingVoice)
class TrainingVoiceAdmin(admin.ModelAdmin):
    list_display = (
        'savedDate',
        'voiceFile',
        'length',
        'lesson',
    )


@admin.register(FeedBackVoice)
class FeedbackVoiceAdmin(admin.ModelAdmin):

    list_display = (
        'voiceFile',
        'savedDate',
        'subject',
        'lesson',
    )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'author',
        'published_date',
    )

@admin.register(HomeWorkVoice)
class HomeWorkVoiceAdmin(admin.ModelAdmin):
    list_display = (
        'voiceFile',
        'savedDate',
        'lesson',
    )


# admin.register(Vocal,VocalAdmin)
admin.register(TrainingVoice,TrainingVoiceAdmin)
admin.register(FeedBackVoice,FeedbackVoiceAdmin)
admin.register(HomeWorkVoice,HomeWorkVoiceAdmin)
admin.register(Post,PostAdmin)


# Register your models here.
