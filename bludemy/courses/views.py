from datetime import datetime
from django.shortcuts import render_to_response, RequestContext, Http404, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from enrollments.models import Enrollment
from enrollments.decorators import enrolled_required
from .models import Course, Lesson, Live

@login_required
def index(request):
	courses = request.user.get_my_active_courses()
	return render_to_response('courses/index.html', {'courses': courses }, context_instance=RequestContext(request))

@login_required
@enrolled_required
def view_course(request,course_slug):
	course = get_object_or_404(Course, slug=course_slug)
	live_sessions = Live.objects.filter(section__course_id=course.id, active=True)
	today_date = datetime.today().date()
	return render_to_response('courses/course.html', {'course': course, 'live_sessions': live_sessions, 'today_date': today_date}, context_instance=RequestContext(request))

@login_required
@enrolled_required
def view_lesson(request,course_slug,lesson_slug):
	lesson = get_object_or_404(Lesson, slug=lesson_slug)
	return render_to_response('courses/lesson.html', {'lesson': lesson, 'disqus_shortname': settings.DISQUS_SHORTNAME }, context_instance=RequestContext(request))


@login_required
def lesson_completed(request):
	if request.POST and request.user.is_authenticated:
		lesson = get_object_or_404(Lesson, pk=request.POST['lesson_id'])
		lesson.user_completed_lessons.add(request.user)

	return redirect('view_course', course_slug=lesson.section.course.slug)


@login_required
@enrolled_required
def view_live(request,course_slug,live_id):
	live = get_object_or_404(Live, pk=live_id)
	return render_to_response('courses/live.html', {'live': live, 'disqus_shortname': settings.DISQUS_SHORTNAME }, context_instance=RequestContext(request))
