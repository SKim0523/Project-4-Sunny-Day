from django.urls import path
from . import views

urlpatterns = [
    #This is to display today and tomorrow's schedule
    path('daily/', views.DailySchedule.as_view(), name="daily_schedule"), 
    #This is to creaete a new day
    path('day/new', views.DayCreate.as_view(), name="day_create"),
    #This is to update a day's content
    path('day/<int:pk>/update',
        views.DayUpdate.as_view(), name="day_update"),
    #This is to delete the day (delete everything for the day)
    path('day/<int:pk>/delete',
        views.DayDelete.as_view(), name="day_delete"),
    #This is to create a new schedule (part of a day)
    path('schedule/new', views.ScheduleCreate.as_view(), name="schedule_create"),
    #This is to update a schedule
    path('schedule/<int:pk>/update',
        views.ScheduleUpdate.as_view(), name="schedule_update"),
    #This is to delete a schedule
    path('schedule/<int:pk>/delete',
        views.ScheduleDelete.as_view(), name="schedule_delete"),
    #This is to display relevant week's
    path('weekly/', views.WeeklySchedule.as_view(), name="weekly_schedule")
]