# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'nickname',
    )

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'nickname',
    )

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'teacher',
        'current',
    )



admin.register(Student,StudentAdmin)
admin.register(Teacher,TeacherAdmin)
admin.register(Lesson,LessonAdmin)

# Register your models here.
