from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    EmpName = forms.CharField(label='Employee Name',max_length=100)
    EmpId = forms.CharField(label='Employee Id',max_length=30)
