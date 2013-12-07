from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField


class Course(models.Model):
	title = models.CharField(max_length=240)
	slug = AutoSlugField(populate_from='title', editable=True, overwrite=True) #This is Unique
	description = models.TextField(default='Your description')
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
	    return reverse_lazy('view_course', args=[self.slug])


class Section(models.Model):
	title = models.CharField(max_length=240)
	slug = AutoSlugField(populate_from='title', editable=True, overwrite=True) #This is Unique
	course = models.ForeignKey(Course, related_name='sections')
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
	    return reverse_lazy('view_course', args=[self.course.slug])


class Lesson(models.Model):
	title = models.CharField(max_length=240)
	slug = AutoSlugField(populate_from='title', editable=True, overwrite=True) #This is Unique
	description = models.CharField(max_length=244, blank=True)
	section = models.ForeignKey(Section, related_name='lessons')
	user_completed_lessons = models.ManyToManyField(User, blank=True)
	content = models.TextField()
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

	def is_completed_by_user(self,user_id):
		return self.user_completed_lessons.filter(id=user_id).count() > 0

	def get_absolute_url(self):
	    return reverse_lazy('view_lesson', args=[self.section.course.slug, self.slug])


class Live(models.Model):
	title = models.CharField(max_length=240)
	slug = AutoSlugField(populate_from='title', editable=True, overwrite=True) #This is Unique
	description = models.CharField(max_length=244, blank=True)
	section = models.ForeignKey(Section, related_name='live_sessions')
	content = models.TextField()
	active = models.BooleanField(default=True)
	start_date = models.DateTimeField()
	enable_chat = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

	def get_chat_uuid(self):
		return self.slug+'-'+str(self.id)

	def get_absolute_url(self):
	    return reverse_lazy('view_live', args=[self.section.course.slug, self.id])