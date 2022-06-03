from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('schedules/', views.ScheduleList.as_view(), name="schedule_list")
]