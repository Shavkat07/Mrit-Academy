from django.db import models


class Progress(models.Model):
    user = models.ForeignKey("users.User", verbose_name="Student", on_delete=models.CASCADE)
    # course = models.ForeignKey("course.Course", verbose_name="Kurs", on_delete=models.CASCADE)
    exercise_category = models.ForeignKey("exercises.ExerciseCategory", verbose_name="Vazifa turi",
                                          on_delete=models.CASCADE)
    exercise_ids = models.TextField(verbose_name="Tugatgan vazifalar id lari", null=True, blank=True)
    completed_exercise = models.IntegerField(verbose_name="Bajargan vazifalar soni", default=0)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Progres"
        verbose_name_plural = "Progreslar"
