from django.urls import path
from .views import *

app_name = 'exercises'

urlpatterns = [
    path('exercise/<int:exercise_id>/', ExerciseView, name='exercises')
]
