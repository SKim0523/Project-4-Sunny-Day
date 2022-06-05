from django.contrib import admin
from .models import User, Day, Schedule

# Register your models here.
admin.site.register(Day)
admin.site.register(Schedule)