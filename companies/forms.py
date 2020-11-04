from django import forms 
from .import models



class AddCompany(forms.ModelForm):
    class Meta:
        model= models.Company
        fields = ['company_name','staff_name','staff_number']