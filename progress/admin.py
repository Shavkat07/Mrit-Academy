from django.contrib import admin
from .models import Progress


@admin.register(Progress)
class Progress(admin.ModelAdmin):
    list_display = ('user', 'exercise_category', 'completed_exercise')
