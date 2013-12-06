from django import template

register = template.Library()

@register.filter(name='is_completed_by_user')
def is_completed_by_user(lesson, user_id):
    return lesson.is_completed_by_user(user_id)