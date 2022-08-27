from django.contrib import admin

from todo.models import Task


# Organiser la vue dans l'administration
class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'task_done', 'created_on', 'updated_on')
    fieldsets = [
        (None, {'fields': ['author', 'title', 'task_done']}),
        ('Descriptions', {'fields': ['description']})
    ]


admin.site.register(Task, TaskAdmin)
