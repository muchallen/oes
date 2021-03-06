# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms 

# Create your models here.

class Exam(models.Model):
    name = models.SlugField()
    time = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    questions_number = models.IntegerField(default=0)
    instructions = models.TextField()
    def __str__(self):
        return self.name
    def snippet_description(self):
        return self.description[:20]

class Question(models.Model):
    question_number = models.IntegerField(default=0)
    image= models.ImageField(upload_to='images/',blank=True, null=True)
    question = models.TextField()
    exam=models.ForeignKey(Exam, default=None)

class SolutionsText(models.Model):
    question_number = models.IntegerField(default=0)
    possible_solution_a = models.CharField(max_length=1000)
    possible_solution_b = models.CharField(max_length=1000, null=True,blank=True)
    possible_solution_c = models.CharField(max_length=1000,null=True,blank=True)
    possible_solution_d = models.CharField(max_length=1000,null=True,blank=True)
    exam=models.ForeignKey(Exam, default=None)
    
    
class CorrectSolution(models.Model):
    question_number = models.IntegerField(default=0)
    correct_solution_letter = models.CharField(max_length=1)
    exam=models.ForeignKey(Exam, default=None)
    