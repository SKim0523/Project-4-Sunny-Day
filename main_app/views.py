from django.shortcuts import render
from django.shortcuts import redirect
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


class DayCreate(CreateView):
    model = Day
    fields = ['date', 'memo']
    template_name = "day_create.html"
    def get_success_url(self):
        return redirect('day_create', kwargs={'pk': self.object.pk})

class ScheduleCreate(CreateView):
    model = Schedule
    fields = ['time', 'content']
    template_name = "schedule_create.html"
    def get_success_url(self):
        return redirect('schedule_create', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['time', 'content']
    template_name = "schedule_update.html"
    success_url = "/daily/"
    
@method_decorator(login_required, name='dispatch')    
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

@method_decorator(login_required, name='dispatch')
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
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("daily_schedule")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
