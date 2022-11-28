import datetime
from django.views.generic import CreateView, TemplateView, UpdateView
from .models import Attendance, UserProfile
from django.contrib.auth.models import User
# Create your views here.
class IndexTemplateView(CreateView):
	template_name = 'index.html'
	model = UserProfile
	fields = ['profile_photo', 'contact_no', 'description']
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(IndexTemplateView, self).get_context_data(**kwargs)
		context['last_attendance'] = Attendance.objects.filter(user=self.request.user).last()
		context['today'] = datetime.datetime.now().date()
		return context
	
	def form_valid(self, form):
		instance = form.save(commit=False)
		try:
			us = User.objects.create(username=self.request.POST['username'], first_name=self.request.POST['first_name'],
			                                    last_name=self.request.POST['last_name'], email=self.request.POST['email'])
			us.set_password(self.request.POST['password'])
			us.save()
			instance.user = us
			return super(IndexTemplateView, self).form_valid(form)
		except:
			return super(IndexTemplateView, self).form_invalid(form)

class AttendanceCreateView(CreateView):
	model = Attendance
	fields = []
	success_url = '/'
	template_name = 'index.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(AttendanceCreateView, self).form_valid(form)

class AttendanceUpdateView(UpdateView):
	model = Attendance
	fields = []
	success_url = '/'
	template_name = 'index.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.out_time = datetime.datetime.now()
		return super(AttendanceUpdateView, self).form_valid(form)