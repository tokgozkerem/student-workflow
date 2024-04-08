import html
from datetime import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm, AssignmentForm, TaskForm
from .models import Course, Assignment, Pomodoro, Task
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta


# Create your views here.
def home_view(request):
    return render(request, "home.html")


def add_course_view(request):
    if request.method == "POST":
        course_id = request.POST.get("courseID")
        course_name = request.POST.get("courseName")
        course_credit = request.POST.get("courseCredit")
        course_date = request.POST.get("courseDate")
        course_length = request.POST.get("courseLength")
        course_instructor = request.POST.get("courseInstructor")
        course_place = request.POST.get("coursePlace")

        # Veritabanına yeni dersi kaydet
        new_course = Course(
            course_id=course_id,
            course_name=course_name,
            course_credit=course_credit,
            course_date=course_date,
            course_length=course_length,
            course_instructor=course_instructor,
            course_place=course_place,
        )
        new_course.save()

        # Yeni ders eklendikten sonra anasayfaya yönlendir
        return HttpResponseRedirect("/")
    else:
        form = CourseForm()

    # Veritabanından tüm dersleri çek
    courses = Course.objects.all()
    return render(request, "add-course.html", {"form": form, "courses": courses})


def add_assignment_view(request):
    if request.method == "POST":
        course = request.POST.get("assignment_course")
        title = request.POST.get("assignment_title")
        deadline = request.POST.get("assignment_deadline")

        if course and title and deadline:
            # Yeni atamayı kaydet
            new_assignment = Assignment.objects.create(
                assignment_course=course,
                assignment_title=title,
                assignment_deadline=deadline,
            )
            # Yeni atamanın id'sini döndür
            return JsonResponse({"id": new_assignment.id})
    else:
        # Tüm atamaları al
        assignments = Assignment.objects.all()
        # Remaining days hesaplaması
        for assignment in assignments:
            assignment.remaining_days = (
                assignment.assignment_deadline - datetime.now().date()
            ).days
        # Atamaları "add-assignment.html" dosyasına aktar ve sayfayı render et
        return render(request, "add-assignment.html", {"assignments": assignments})


def delete_assignment_view(request):
    if request.method == "POST":
        assignment_id = request.POST.get("assignment_id")
        if assignment_id:
            # Görevi sil
            try:
                assignment = Assignment.objects.get(id=assignment_id)
                assignment.delete()
                return JsonResponse({"message": "Assignment deleted successfully."})
            except Assignment.DoesNotExist:
                return JsonResponse({"error": "Assignment does not exist."}, status=404)
    return JsonResponse({"error": "Invalid request."}, status=400)


def start_pomodoro(request):
    if request.method == "POST":
        duration = int(request.POST["duration"])
        end_time = timezone.now() + timedelta(minutes=duration)
        Pomodoro.objects.create(duration=duration, end_time=end_time)
        return redirect("pomodoro:home")
    return render(request, "pomodoro.html")


def todo_list(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TaskForm()
    return render(request, "todo_list.html", {"tasks": tasks, "form": form})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect("todo_list")


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TaskForm(instance=task)
    return render(
        request, "todo_list.html", {"tasks": Task.objects.all(), "form": form}
    )
