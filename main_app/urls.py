from django.urls import path, include
from . import views

urlpatterns = [
    #This is to display today and tomorrow's schedule
    path('daily/', views.DailySchedule.as_view(), name="daily_schedule"), 
    #This is to creaete a new day
    
    path('day/new', views.DayCreate.as_view(), name="day_create"),
    #This is to delete the day (delete everything for the day)
     path('schedule/new', views.ScheduleCreate.as_view(), name="schedule_create"),
    #This is to update a schedule
    
    
    path('memo/<int:pk>/update',
        views.MemoUpdate.as_view(), name="memo_update"),
    path('schedule/<int:pk>/update',
        views.ScheduleUpdate.as_view(), name="schedule_update"),
    #This is to update memo content
    
    
    path('day/<int:pk>/delete',
        views.DayDelete.as_view(), name="day_delete"),
    #This is to create a new schedule (part of a day)
     #This is to delete a schedule
    path('schedule/<int:pk>/delete',
        views.ScheduleDelete.as_view(), name="schedule_delete"),
   
    
    #This is to display relevant week's
    path('weekly/', views.WeeklySchedule.as_view(), name="weekly_schedule"),
    
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]