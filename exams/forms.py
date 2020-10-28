from django import forms 
from .import models




class CreateExam(forms.ModelForm):
    class Meta:
        model= models.Exam
        fields = ['name','time','questions_number','instructions']

class CreateQuestion(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['question_number','exam','question','image']

class CreateSolution(forms.ModelForm):
    class Meta:
        model = models.SolutionsText
        fields = ['possible_solution_a','possible_solution_b','possible_solution_c','possible_solution_d','exam']

class CorrectSolution(forms.ModelForm):
    class Meta:
        model = models.CorrectSolution
        fields = ['correct_solution_letter','exam']
        
    
    