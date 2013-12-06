from django.contrib import admin
from .models import Enrollment


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['course','user','start_date','end_date',]


admin.site.register(Enrollment,EnrollmentAdmin)