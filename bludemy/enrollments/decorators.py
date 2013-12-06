from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import PermissionDenied
from courses.models import Course
from .utils import get_object_or_none
from .models import Enrollment


# Check if is enrolled in the course.
# The View function must have a course_slug KeyWordArg
def enrolled_required(funcion):
	def wrapper(*args, **kwargs):
		request = args[0]
		if 'course_slug' in kwargs:
			enrollment = get_object_or_none(Enrollment, user_id=request.user.id, course_id=get_object_or_404(Course,slug=kwargs['course_slug']).id)
			user_active_enrollments = request.user.get_active_enrollments()
			if enrollment in user_active_enrollments:
				# You are enrolled in the course
				return funcion(*args, **kwargs)
			else: 
				# You are Not Enrolled in the course
				raise PermissionDenied
		raise Http404
	return wrapper
