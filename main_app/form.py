from django.forms import forms
from .models import Day, Schedule

class ScheduleForm(forms.ModelForm):
    # create_schedule = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Schedule
        fields = ['date', 'time', 'schedule']
        
class MemoForm(forms.ModelForm):
#    create_memo = forms.BooleanField(widget=forms.HiddenInput, initial=True)
   
   class Meta:
        model = Day
        fields = ['date', 'memo']