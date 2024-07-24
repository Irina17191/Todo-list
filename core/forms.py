from django import forms
from core.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            }
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"

