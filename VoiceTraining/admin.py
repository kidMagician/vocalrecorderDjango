# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# @admin.register(Vocal)
# class VocalAdmin(admin.ModelAdmin):
#     list_display = (
#         'youtubeUrl',
#         'name',
#         'student',
#     )


@admin.register(TrainingVoice)
class TrainingVoiceAdmin(admin.ModelAdmin):
    list_display = (
        'savedDate',
        # 'vocal',
        'voice',
    )


# admin.register(Vocal,VocalAdmin)
admin.register(TrainingVoice, TrainingVoiceAdmin)



# Register your models here.
