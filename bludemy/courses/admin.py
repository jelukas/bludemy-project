from django import forms
from django.db import models
from django.contrib import admin
from redactor.widgets import RedactorEditor
from .models import Course, Section, Lesson, Live


class BsRedactorEditor(RedactorEditor):
    def __init__(self, *args, **kwargs):
        super(BsRedactorEditor, self).__init__(*args, **kwargs)
        self.Media.js = (
            'redactor/redactor.js',
        )
 

class SectionInline(admin.TabularInline):
	model = Section


class SectionAdmin(admin.ModelAdmin):
	pass


class LessonAdmin(admin.ModelAdmin):
    # your model definition here
    formfield_overrides = {
       models.TextField: {'widget': BsRedactorEditor},
    }


class LiveAdmin(admin.ModelAdmin):
    # your model definition here
    formfield_overrides = {
       models.TextField: {'widget': BsRedactorEditor},
    }


class CourseAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	inlines = [SectionInline,]




admin.site.register(Course,CourseAdmin)
admin.site.register(Section,SectionAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Live,LiveAdmin)