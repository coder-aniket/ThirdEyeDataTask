from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .api import *

urlpatterns = [
	path('', login_required(views.IndexTemplateView.as_view()), name="index"),
	path('login', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
	path('logout', login_required(auth_views.LogoutView.as_view(template_name='login.html')), name="logout"),
	path('check_in', login_required(views.AttendanceCreateView.as_view()), name="check_in"),
	path('check_out/<int:pk>', login_required(views.AttendanceUpdateView.as_view()), name="check_out"),
	path('api/my_attendance', login_required(MyAttendanceListAPIView.as_view()), name="my_attendance-api"),
	path('api/all_attendance', login_required(AllAttendanceListAPIView.as_view()), name="all_attendance-api"),
]