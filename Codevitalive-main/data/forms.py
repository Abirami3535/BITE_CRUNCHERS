from email.policy import default
from random import choices
from django import forms

class UserForm(forms.Form):
    Male="male"
    Female="Female"
    Other="other"
    CHOICES = [
        (Male, 'male'),
        (Female, 'Female'),
        (Other, 'other'),
        
    ]
    first_name= forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    date=forms.DateField()
    gender=forms.CharField(max_length=100)
    mail=forms.CharField(max_length=200)
    in_name=forms.CharField(max_length=100)
    qualification=forms.CharField(max_length=50)
    linkedin=forms.CharField(max_length=100)
    github=forms.CharField(max_length=100) 
    department=forms.CharField(max_length=100)
    
  
    

    
