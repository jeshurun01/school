from django.contrib import admin

from todo.models import Task


# Organiser la vue dans l'administration
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'task_done', 'slug', 'created_on', 'updated_on')
    fieldsets = [
        (None, {'fields': ['author', 'title', 'slug', 'task_done']}),
        ('Descriptions', {'fields': ['description']})
    ]
    prepopulated_fields = {
        'slug': ('title',)
    }



