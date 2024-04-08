from django import forms
from .models import Course, Assignment, Task


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "course_id",
            "course_name",
            "course_credit",
            "course_date",
            "course_length",
            "course_instructor",
            "course_place",
        ]


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["assignment_course", "assignment_title", "assignment_deadline"]
        widgets = {"assignment_deadline": forms.DateInput(attrs={"type": "date"})}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
