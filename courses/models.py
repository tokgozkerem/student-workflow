from django.db import models

# Create your models here.


class Course(models.Model):
    course_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    course_credit = models.CharField(max_length=2, default="3")
    course_date = models.CharField(max_length=10)
    course_length = models.IntegerField(default=0)
    course_instructor = models.CharField(max_length=50)
    course_place = models.CharField(max_length=50)


class Assignment(models.Model):
    assignment_course = models.CharField(max_length=50)
    assignment_title = models.CharField(max_length=250)
    assignment_deadline = models.DateField()


class Pomodoro(models.Model):
    duration = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} dakika") for i in range(10, 121, 5)]
    )
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
