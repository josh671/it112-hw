from django import forms
from django.forms import fields
from django.forms.models import ModelForm 
from .models import Meeting, MeetingMinutes, Resources, Event

class MeetingForm(forms.ModelForm): 
    class Meta: 
        #specifies fields you want 
        model=Meeting 
        fields='__all__' 

class ResourceForm(forms.ModelForm): 
    class Meta: 
        #specifies fields you want 
        model=Resources 
        fields='__all__' 
        