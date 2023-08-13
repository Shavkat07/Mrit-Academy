from django.db import models

from users.models import User
from .convert import is_ipynb


# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    course_description = models.TextField()

    # price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # views = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name


class CourseChapter(models.Model):
    chapter_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter_content_ipynb = models.FileField(upload_to='ipynb_notebooks/', validators=[is_ipynb])

    def __str__(self):
        return f'{self.course.course_name} - {self.chapter_name}'
