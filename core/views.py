from django.shortcuts import render
from django.http import HttpResponse
import datetime

from . import models


def index(request):
    schools = models.School.objects.all()
    return render(request, 'core/index.html', {'schools': schools, 'title': 'Список школ'})


def get_teachers(request):
    teachers = models.Teacher.objects.all()
    return render(request, 'core/teachers.html', {'teachers': teachers, 'title': 'Список учителей'})


def get_groups(request):
    groups = models.Group.objects.all()
    return render(request, 'core/groups.html', {'groups': groups, 'title': 'Список классов'})
