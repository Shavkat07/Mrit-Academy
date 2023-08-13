from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from .models import Exercise
from progress.models import Progress
from django.db.models import F


# Create your views here.
def ExerciseView(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)

    true_answer = exercise.answer.split()

    len_answer = len(max(true_answer, key=len)) + 2

    code = exercise.code

    context = {
        'exercise': exercise,
        'code': code,
        'exercise_id': exercise_id,
        'len': len_answer,
    }
    if request.method == 'POST':
        answers_list = request.POST.getlist('answer_data')

        if answers_list == true_answer:
            context['success_message'] = "Tabriklaymiz Javobingiz To'g'ri"
            progress = Progress.objects.filter(user=request.user, exercise_category=exercise.category)
            if progress.exists():
                print("Progress mavjud  ")
                progress = get_object_or_404(Progress, user=request.user, exercise_category=exercise.category)
                existing_exercise_ids = progress.exercise_ids

                if f'{exercise_id}' in existing_exercise_ids.split(', '):
                    new_exercise_ids = str(existing_exercise_ids)
                else:
                    new_exercise_ids = f"{existing_exercise_ids}, {exercise_id}"
                    progress.completed_exercise = F('completed_exercise') + 1
                progress.exercise_ids = new_exercise_ids
                progress.save()
            elif not progress.exists():
                Progress.objects.create(user=request.user, exercise_category=exercise.category,
                                        exercise_ids=f'{exercise_id}', completed_exercise=1)

            return render(request, 'exercises/exercise_page.html', context=context)
        else:
            context['error_message'] = "Javobingiz noto'g'ri"
            return render(request, 'exercises/exercise_page.html', context=context)

    return render(request, 'exercises/exercise_page.html', context=context)
