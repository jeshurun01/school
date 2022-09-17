from django.contrib import admin

from .models import Profile


# Organiser la vue dans l'administration
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography', 'created', 'updated')
    fieldsets = [
        (None, {'fields': ['user', 'avatar']}),
        ('Biographie', {'fields': ['biography']})
    ]


admin.site.register(Profile, ProfileAdmin)
