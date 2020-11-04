# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import View

from django.shortcuts import render,redirect
from . import forms
from . import models



#Global Variables 
totalquestions=0
count=1


# Create Exam 
def create_exam(request):
    global count
    global totalquestions
    count=1
    if(request.method=='POST'):
        form = forms.CreateExam(request.POST)
        if(form.is_valid()):
            form.save()
            exam=request.POST.get('name')
            totalquestions=int(request.POST.get('questions_number'))
            return redirect('/exams/createQuestion/'+exam)
        else:
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
def delete_exam(request,slug):
    models.Exam.objects.filter(name=slug).delete()
    exams = models.Exam.objects.all()
    return render(request, 'exams/exams.html',{'exams':exams})

def edit_question(request,exam,number): 
    exam1= models.Exam.objects.get(name=exam)
    question = models.Question.objects.get(exam=exam1,question_number=number)    
    solution = models.SolutionsText.objects.get(exam=exam1,question_number=number)
    corect_answer= models.CorrectSolution.objects.get(exam=exam1,question_number=number)
    form_question= forms.CreateQuestion(initial={'question_number':question.question_number,'question':question.question,'image':question.image, 'exam':question.exam})
    form_solutions= forms.CreateSolution(initial={
    'question_number':solution.question_number,
    'possible_solution_a':solution.possible_solution_a,
    'possible_solution_b':solution.possible_solution_b,
    'possible_solution_c':solution.possible_solution_c,
    'possible_solution_d':solution.possible_solution_d,
    'exam':solution.exam
    })
    form_correct_solution=forms.CorrectSolution(initial={'question_number':corect_answer.question_number,
    'correct_solution_letter':corect_answer.correct_solution_letter,
    'exam':corect_answer.exam})

    return render (request, 'exams/edit_exam.html', {'form':form_question,'formsolution':form_solutions,'form_correct_solution':form_correct_solution})

def update_question(request):
     if(request.method=="POST"):
        question = request.POST.get('question')
        question_number = request.POST.get('question_number')
        exam=request.POST.get('exam')
        possible_solution_a=request.POST.get('possible_solution_a')
        possible_solution_b=request.POST.get('possible_solution_b')
        possible_solution_c=request.POST.get('possible_solution_c')
        possible_solution_d=request.POST.get('possible_solution_d')
        correct_solution_letter=request.POST.get('correct_solution_letter')

        models.Question.objects.filter(question_number=question_number, exam=exam).update(question=question)
        models.SolutionsText.objects.filter(question_number=question_number, exam=exam).update(
        possible_solution_a=possible_solution_a, 
        possible_solution_b=possible_solution_b,
        possible_solution_c=possible_solution_c,
        possible_solution_d=possible_solution_d
        )
        models.CorrectSolution.objects.filter(question_number=question_number, exam=exam).update(correct_solution_letter=correct_solution_letter)

        print(question,exam,question_number)

        return render (request, 'exams/view_exam.html')
def create_question_form(request,exam):
    global count
    global totalquestions
    exam1= models.Exam.objects.get(name=exam)
    

    if(request.method=="POST"):
        


        print(request.POST)
        question_object = models.Question()
        solution_object = models.SolutionsText()
        correct_answer_object = models.CorrectSolution()

        #set question object 
       

        
        question_object.exam = exam1
        question_object.question=request.POST.get('question')
        question_object.question_number=count
        question_object.image=request.POST.get('image')
        question_object.save()

        #set solution object
        solution_object.exam=exam1
        solution_object.question_number=count
        solution_object.possible_solution_a= request.POST.get('possible_solution_a')
        solution_object.possible_solution_b= request.POST.get('possible_solution_b')
        solution_object.possible_solution_c= request.POST.get('possible_solution_c')
        solution_object.possible_solution_d= request.POST.get('possible_solution_d')
        solution_object.save()


        # form_question_vals= forms.CreateSolution(
        #     initial={
        #         'possible_solution_a':request.POST.get('possible_solution_a'),
        #         'possible_solution_b':request.POST.get('possible_solution_b'),
        #         'possible_solution_c':request.POST.get('possible_solution_c'),
        #         'possible_solution_d':request.POST.get('possible_solution_d'),
        #         'question_number':count,
        #         'exam':exam1
        #     }
        # )
        # if(form_question_vals.is_valid()):
        #     form_question_vals.save()
        #     print('saved everything')

        #set correct answer object
        correct_answer_object.exam=exam1
        correct_answer_object.correct_solution_letter=request.POST.get('correct_solution_letter')
        correct_answer_object.question_number=count
        correct_answer_object.save()

        count=count+1
        if(count<=totalquestions):
            form_question= forms.CreateQuestion(initial={'exam':exam1,'question_number':count})
            form_solutions= forms.CreateSolution(initial={'exam':exam1,'question_number':count})
            form_answer =  forms.CorrectSolution(initial={'exam':exam1,'question_number':count})
            return render(request,'exams/create_question.html',{"form_question":form_question, "form_solutions":form_solutions, "form_answer":form_answer , 'exam':exam1})
        else:
            return redirect('/exams')
    
    else:
        form_question= forms.CreateQuestion(initial={'exam':exam1,'question_number':count})
        form_solutions= forms.CreateSolution(initial={'exam':exam1,'question_number':count})
        form_answer =  forms.CorrectSolution(initial={'exam':exam1,'question_number':count})
        return render(request,'exams/create_question.html' ,{"form_question":form_question, "form_solutions":form_solutions, "form_answer":form_answer,'exam':exam1})



    


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

   