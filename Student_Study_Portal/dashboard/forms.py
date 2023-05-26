
from dataclasses import fields
from random import choices
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','description']
    
class DateInput(forms.DateInput):
    input_type='date'

    
class Homeworkform(forms.ModelForm):
    class Meta:
        model=Homework
        widgets={'due':DateInput()}
        fields={'subject','title','description','due','is_finished'}

class Dashboardform(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search  ")


class Todoform(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']

class Conversionform(forms.Form):
   CHOICES=[('length','Length'),('mass','Mass')]
   measurement=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES=[('yard','Yard'),('foot','Foot')]
    input=forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the number'}
    ))
    measure1=forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    measure2=forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )

class ConversionMassForm(forms.Form):
    CHOICES=[('pound','Pound'),('kilogram','Kilogram')]
    input=forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the number'}
    ))
    measure1=forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    measure2=forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )

class UserRegistrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']