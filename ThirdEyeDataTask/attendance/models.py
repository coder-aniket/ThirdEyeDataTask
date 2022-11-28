from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_photo = models.FileField(upload_to="media/user_profile/")
	contact_no = models.PositiveBigIntegerField(validators=[MinValueValidator(7000000000), MaxValueValidator(9999999999)])
	description = models.CharField(max_length=25, null=True, blank=True)

	def __str__(self):
		return self.user.get_full_name()


class Attendance(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	in_time = models.DateTimeField(auto_now_add=True)
	out_time = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.user.get_full_name()
