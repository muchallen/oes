# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Exam,Question,SolutionsText,CorrectSolution

# Register your models here.

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(SolutionsText)
admin.site.register(CorrectSolution)