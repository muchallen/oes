from django import forms 
from .import models




class AddTestee(forms.ModelForm):
    class Meta:
        model= models.Testee
        fields = ['first_name','last_name','id_number','email','company']