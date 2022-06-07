
from django.views.generic.base import TemplateView
from .models import Day, Schedule
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from datetime import datetime, timedelta, time


class DayCreate(CreateView):
    model = Day
    fields = ['date', 'memo']
    template_name = "day_create.html"
    def get_success_url(self):
        return reverse('daily_view', kwargs={'pk': self.object.pk})

class ScheduleCreate(CreateView):
    model = Schedule
    fields = ['time', 'content']
    template_name = "schedule_create.html"
    def get_success_url(self):
        return reverse('daily_view', kwargs={'pk': self.object.pk})

class DayUpdate(UpdateView):
    model = Day
    fields = ['date', 'memo']
    template_name = "day_create.html"
    success_url = "/daily/"

class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['time', 'content']
    template_name = "schedule_update.html"
    success_url = "/daily/"
    
class MemoUpdate(UpdateView):
    model = Day
    fields = ['memo']
    template_name = "memo_update.html"
    success_url = "/daily/"   
    
class DayDelete(DeleteView):
    model = Day
    template_name = "day_delete.html"
    success_url = "/weekly/"

class ScheduleDelete(DeleteView):
    model = Schedule
    template_name = "schedule_delete.html"
    success_url = "/daily/"

class DailySchedule(TemplateView):
    template_name = "daily_view.html"
    def get_context_data(self, **kwargs):
        # https://stackoverflow.com/questions/11245483/django-filter-events-occurring-today
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        context = super().get_context_data(**kwargs)
        context["days"] = Day.objects.filter(date__in=[today, tomorrow])
        # def get_success_url(self):
        #     return reverse('schedule_update', kwargs={'pk': self.object.pk})
        
        # context["schedule"] = Schedule.objects.filter(day__in=[today, tomorrow])
        # context["memo"] = Day.objects.filter(memo__in=[today, tomorrow])
        
        return context
    
class WeeklySchedule(TemplateView):
    template_name = "weekly_view.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["days"] = Day.objects.all()
        return context