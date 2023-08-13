from django.contrib import admin
from .models import Course, CourseChapter
from .convert import turn_into_html


# Register your models here.

class CourseChapterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        turn_into_html(obj.chapter_content_ipynb, obj.chapter_name)


admin.site.register(Course)
admin.site.register(CourseChapter, CourseChapterAdmin)
