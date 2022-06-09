
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Day, Schedule
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from datetime import datetime, timedelta, time
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from .forms import ScheduleCreateForm, DayCreateForm

# Below saves data to the database
@method_decorator(login_required, name='dispatch')
class DayCreate(View):
    def get(self, request):
        return render(request, "day_create.html")
    
    def post(self, request):
        # return render(request, "daily_view.html")
        date = request.POST.get("date")
        time = request.POST.get("time")
        content = request.POST.get("content")
        memo = request.POST.get("memo")
        dayContent = Day.objects.create(date=date, memo=memo)
        Schedule.objects.create(time=time, content=content, day_id=dayContent.id)
        return redirect('daily_schedule')



class ScheduleCreate(View):
    def get(self, request, day_id, *args, **kwargs):
        print(request.session.items())
        dayId = request.GET.get("day_id")
        print(dayId)
        return render(request, "schedule_create2.html")
    
    def post(self, request):
        time = request.POST.get("time")
        content = request.POST.get("content")
        print(request.day_id)
       
        # Schedule.objects.create(time=time, content=content, day_id=dayId)
        
        return redirect('daily_schedule')
    




@method_decorator(login_required, name='dispatch')
class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['time', 'content', 'day']
    template_name = "schedule_update.html"
    success_url = "/daily/"
    
@method_decorator(login_required, name='dispatch')    
class MemoUpdate(UpdateView):
    model = Day
    fields = ['memo']
    template_name = "memo_update.html"
    success_url = "/daily/"   

@method_decorator(login_required, name='dispatch')
class ScheduleDelete(DeleteView):
    model = Schedule
    template_name = "schedule_delete.html"
    success_url = "/daily/"

@method_decorator(login_required, name='dispatch')
class MemoDelete(DeleteView):
    model = Day
    template_name = "memo_delete.html"
    success_url = "/daily/"
    
# class MemoDelete(View):
#     def get(self, request):
#         Day.objects.get(pk=day_id).update(memo=None)
#         return render(request, "dayily_view.html")

@method_decorator(login_required, name='dispatch')
class DailySchedule(TemplateView):
    template_name = "daily_view.html"
    def get_context_data(self, **kwargs):
        # https://stackoverflow.com/questions/11245483/django-filter-events-occurring-today
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        context = super().get_context_data(**kwargs)
        context["days"] = Day.objects.filter(date__in=[today, tomorrow]) 
        return context

    
class WeeklySchedule(TemplateView):
    template_name = "weekly_view.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.now().date()
        week_start = date - timedelta(date.weekday())
        week_end = week_start + timedelta(6)
        day_of_week = date.isoweekday()
        context["first_day"] = week_start
        context["last_day"] = week_end
        context["week_day"] = day_of_week
        context["days"] = Day.objects.filter(date__range=[week_start, week_end]) 
        return context
    
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("daily_schedule")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
        
class LogOut(TemplateView):
    template_name = "log_off.html"
    success_url = "/"   
