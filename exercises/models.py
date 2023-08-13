from ckeditor import fields
from django.db import models
from learn.models import Course


# Create your models here.

class ExerciseCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course} {self.name}"


class Exercise(models.Model):
    category = models.ForeignKey(ExerciseCategory, on_delete=models.CASCADE)
    question = models.TextField(verbose_name="Exercise question")
    code = models.TextField(verbose_name="Exercise text")
    answer = models.TextField(verbose_name="Exercise answer")

    def __str__(self):
        return f"{self.category}"


