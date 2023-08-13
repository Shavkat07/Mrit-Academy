from django import forms


class ExerciseAnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.TextInput())
