
from rest_framework.generics import ListAPIView
from .serializer import *
from django.db.models import DurationField, F, ExpressionWrapper
from rest_framework.permissions import IsAdminUser, IsAuthenticated
import datetime

class MyAttendanceListAPIView(ListAPIView):
	serializer_class = AttendanceSerializer
	permission_classes = [IsAuthenticated]

	def filter_queryset(self, queryset):
		filter = {}
		if self.request.GET.get("user", None):
			filter['user__username__icontains'] = self.request.GET['user']
		if self.request.GET.get('hr', None):
			filter['hr__gte'] = datetime.timedelta(hours=int(self.request.GET.get('hr')))
		if self.request.GET.get('in_time', None):
			filter['in_time__date'] = self.request.GET['in_time']
		if self.request.GET.get('out_time', None):
			filter['out_time__date'] = self.request.GET['out_time']
		return queryset.filter(**filter)

	def get_queryset(self):
		diff = ExpressionWrapper(F('out_time')-F('in_time'), output_field=DurationField())
		return Attendance.objects.filter(user=self.request.user).annotate(hr=diff).all().order_by('-id')


class AllAttendanceListAPIView(ListAPIView):
	serializer_class = AttendanceSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

	def filter_queryset(self, queryset):
		filter = {}
		if self.request.GET.get("user", None):
			filter['user__username__icontains'] = self.request.GET['user']
		if self.request.GET.get('hr', None):
			filter['hr__gte'] = datetime.timedelta(hours=int(self.request.GET.get('hr')))
		if self.request.GET.get('in_time', None):
			filter['in_time__date'] = self.request.GET['in_time']
		if self.request.GET.get('out_time', None):
			filter['out_time__date'] = self.request.GET['out_time']
		return queryset.filter(**filter)

	def get_queryset(self):
		diff = ExpressionWrapper(F('out_time')-F('in_time'), output_field=DurationField())
		return Attendance.objects.filter().annotate(hr=diff).all().order_by('-id')
