from django.http import JsonResponse
from django.shortcuts import render
from .models import Course


def course_list(request):
    courses = Course.objects.filter(status="published")
    return render(request, "courses/list.html", {"courses": courses})


def course_api(request):
    courses = list(
        Course.objects.filter(status="published").values("title", "capacity")
    )
    return JsonResponse({"courses": courses})