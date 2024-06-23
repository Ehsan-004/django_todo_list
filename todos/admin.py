from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'start_date', 'done']


admin.site.register(Task, TaskAdmin)
