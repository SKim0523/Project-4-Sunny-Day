"""
This contains subclasses of forms.ModelForm and forms.Form
Purpose of these classes is to receive user input and inspect it for errors
If the input is valid these classes will update the database
"""

from django import forms
from .models import Day, Schedule

class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['time', 'content']
