from django.contrib import admin
from .models import UserProfile, Attendance
# Register your models here.

class UserProfileModelAdmin(admin.ModelAdmin):
	list_display = ['user', 'contact_no', 'description', 'profile_photo']

class AttendanceModelAdmin(admin.ModelAdmin):
	list_display = ['user', 'in_time', 'out_time']

admin.site.register(UserProfile, UserProfileModelAdmin)
admin.site.register(Attendance, AttendanceModelAdmin)