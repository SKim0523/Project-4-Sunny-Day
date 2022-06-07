from django import forms
from .models import Day, Schedule

class ScheduleCreateForm(forms.ModelForm):
    # create_schedule = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Schedule
        fields = ['time', 'content']
        
class DayCreateForm(forms.ModelForm):
#    create_memo = forms.BooleanField(widget=forms.HiddenInput, initial=True)
   
   class Meta:
        model = Day
        fields = ['date', 'memo']