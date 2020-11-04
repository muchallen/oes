from django import forms 
from .import models




class CreateExam(forms.ModelForm):
    class Meta:
        model= models.Exam
        fields = ['name','time','questions_number','instructions']

class CreateQuestion(forms.ModelForm):

    class Meta:
        model = models.Question
        widgets={'question_number':forms.TextInput(attrs={'readonly':'readonly'}),
        'exam': forms.HiddenInput()
        }
        fields = ['question_number','exam','question','image']

class CreateSolution(forms.ModelForm):
    class Meta:
        model = models.SolutionsText
        widgets = {'question_number': forms.HiddenInput(),'exam': forms.HiddenInput()}
        fields = ['possible_solution_a','possible_solution_b','possible_solution_c','possible_solution_d','exam']

class CorrectSolution(forms.ModelForm):
    class Meta:
        model = models.CorrectSolution
        widgets = {'correct_solution_letter': forms.HiddenInput(),'exam': forms.HiddenInput()}
        fields = ['correct_solution_letter','exam']
        
    
    