from django import forms
from django.contrib import admin
from .models import ExerciseCategory, Exercise

from ckeditor.widgets import CKEditorWidget


class ExerciseAdminForm(forms.ModelForm):
    question = forms.CharField(widget=CKEditorWidget())
    code = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Exercise
        fields = '__all__'


# @admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    form = ExerciseAdminForm


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseCategory)
