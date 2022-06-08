from django.urls import path, include
from . import views

urlpatterns = [
    
    #This is to display today and tomorrow's schedule
    path('daily/', views.DailySchedule.as_view(), name="daily_schedule"), 
    #This is a form to creaete a new day
    path('day/new', views.DayCreate.as_view(), name="day_create"),
    
    # These are to update a schedule/memo
    path('schedule/<int:pk>/update',
        views.ScheduleUpdate.as_view(), name="schedule_update"),
    path('memo/<int:pk>/update',
        views.MemoUpdate.as_view(), name="memo_update"),
   
      #This is to delete a schedule/memo
    path('schedule/<int:pk>/delete',
        views.ScheduleDelete.as_view(), name="schedule_delete"),
    path('memo/<int:pk>/delete',
        views.MemoDelete.as_view(), name="memo_delete"),
   
    #This is to display relevant week's schedule
    path('weekly/', views.WeeklySchedule.as_view(), name="weekly_schedule"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('', views.LogOut.as_view(), name="logout")
]