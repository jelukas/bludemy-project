from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
from courses.models import Course

class Enrollment(models.Model):
	user = models.ForeignKey(User)
	course = models.ForeignKey(Course)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.course.title + ' - ' + self.user.email


def get_active_enrollments(self):
	now = datetime.now()
	enrollments = Enrollment.objects.filter(Q(user=self),Q(start_date__lte=now),Q(end_date__gt=now)|Q(end_date__isnull=True))
	return enrollments


def get_my_active_courses(self):
	courses = Course.objects.filter(id__in=self.get_active_enrollments().values_list('course_id', flat=True))
	return courses


User.add_to_class('get_active_enrollments', get_active_enrollments)
User.add_to_class('get_my_active_courses', get_my_active_courses)
