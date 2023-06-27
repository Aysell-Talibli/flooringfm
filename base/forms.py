from django import forms 
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'surname', 'email', 'phone', 'message']

class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name', 'email', 'phone']



class HomeApplyForm(forms.ModelForm):
    class Meta:
        model=HomeApply
        fields=['name', 'surname', 'message']

class EmailForm(forms.ModelForm):
    class Meta:
        model=EmailName
        fields=['subscription_email',]
