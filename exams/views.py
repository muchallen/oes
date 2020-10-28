# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import View

from django.shortcuts import render
from . import forms
from . import models



#Global Variables 
totalquestions=0
count=1


# Create Exam 
def create_exam(request):
    global count
    count=1
    if(request.method=='POST'):
        form = forms.CreateExam(request.POST)
        if(form.is_valid()):
            form.save()
            form = forms.CreateQuestion(initial={'exam':request.POST,'question_number':count})
            global totalquestions
            totalquestions =int(request.POST['questions_number'])
            return render(request, 'exams/question.html', {'form':form})
        else:
            print("failed")
            return render(request, 'exams/create_exam.html', {'form':form})

    else:
        form = forms.CreateExam()
        print("failed")
        return render(request, 'exams/create_exam.html', {'form':form})


#Create Question
def create_question(request):
    global count
    global totalquestions

    if(count<=totalquestions):
        if(request.method=='POST'):
            form = forms.CreateQuestion(request.POST,request.FILES)
            if(form.is_valid()):
                form.save()
                form2 = forms.CreateSolution(initial={'exam':request.POST['exam'],})
                return render(request, 'exams/solution.html', {'form':form2})
            else:
                print("error")
                return render(request, 'exams/question.html', {'form':form})
        else:
            form = forms.CreateQuestion()
            return render(request, 'exams/question.html', {'form':form})
    else:return render(request, 'exams/exam.html')


#Create Solution
def create_solution(request):
    if(request.method=='POST'):
        form = forms.CreateSolution(request.POST)
        if(form.is_valid()):
            form.save()
            form = forms.CorrectSolution(initial={'exam':request.POST['exam']})
            return render(request, 'exams/answer.html', {'form':form})
        else:
            print("error")
            return render(request, 'exams/solution.html', {'form':form})
    else:
        form = forms.CreateSolution()
        return render(request, 'exams/solution.html', {'form':form})

def create_answer(request):
    global count
    global totalquestions
    if(request.method=='POST'):
        form = forms.CorrectSolution(request.POST)
        if(form.is_valid()):
            form.save()
            count=count+1
            if(count<=totalquestions):
                form=forms.CreateQuestion(initial={'question_number':count, 'exam':request.POST['exam']})
                return render(request, 'exams/question.html',{'form':form})
            else:
                return render(request, 'exams/addtest.html')  
        else:
            print("error")
            return render(request, 'exams/answer.html', {'form':form})
    else:
        form = forms.CorrectSolution()
        return render(request, 'exams/answer.html', {'form':form})

def view_full_exam(request,slug):
    exam1= models.Exam.objects.get(name=slug)
    questions = models.Question.objects.filter(exam=exam1)
    solutions = models.SolutionsText.objects.filter(exam=exam1)
    corectanswers= models.CorrectSolution.objects.filter(exam=exam1)

    combinedlist = zip(questions,solutions,corectanswers)
    print(questions)
    return render (request, 'exams/view_exam.html', {'combined':combinedlist, "exam":exam1 }) 

    
def assign_exam(request,slug):
    exam1= models.Exam.objects.get(name=slug)
    questions = models.Question.objects.filter(exam=exam1)
    solutions = models.SolutionsText.objects.filter(exam=exam1)
    corectanswers= models.CorrectSolution.objects.filter(exam=exam1)
    combinedlist2 = zip(questions,solutions)
    
    return render (request, 'exams/assign_exam.html',{'data':combinedlist2,'exam':exam1,'answers':corectanswers} ) 

def mark_exam(request):
    if(request.method=="POST"):
        print(request.POST)
    return HttpResponse("marked")

#Exam List
class ExamView(View):
    def get(self, request, *args, **kwargs):
        exams = models.Exam.objects.all()
        print(exams)
        return render(request, 'exams/exams.html',{'exams':exams})

    # def post(request):
    #     return render(request, 'exams/edittest.html')

    # def addTest(request):
    #     return render(request, 'exams/addtest.html')

   