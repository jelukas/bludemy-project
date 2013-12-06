from django.conf.urls import patterns, include, url
from .views import index, view_course, view_lesson, lesson_completed, view_live

urlpatterns = patterns('',
    url(r'^$', index, name='courses_index'),
    url(r'^(?P<course_slug>[\w-]+)/live/(?P<live_id>[\d]+)$', view_live, name='view_live'),
    url(r'^(?P<course_slug>[\w-]+)/(?P<lesson_slug>[\w-]+)$', view_lesson, name='view_lesson'),
    url(r'^(?P<course_slug>[\w-]+)$', view_course, name='view_course'),
    url(r'^mark_lesson_completed/$', lesson_completed, name='lesson_completed'),
)