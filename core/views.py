from django.shortcuts import render
from django.http import HttpResponse
import datetime

from . import models


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'core/index.html', context)


def get_all_schools(request):
    schools = models.School.objects.all()
    context = {
        'schools': schools,
        'title': 'Список классов'
    }
    return render(request, 'core/schools.html', context)


def get_all_teachers(request):
    teachers = models.Teacher.objects.all()
    context = {
        'teachers': teachers,
        'title': 'Список классов'
    }
    return render(request, 'core/teachers.html', context)


def get_all_groups(request):
    groups = models.Group.objects.all()
    context = {
        'groups': groups,
        'title': 'Список классов'
    }
    return render(request, 'core/groups.html', context)


def get_group(request, group_id):
    students = models.Student.objects.filter(group=group_id)
    groups = models.Group.objects.all()
    group = models.Group.objects.get(pk=group_id)

    context = {
        'students': students,
        'groups': groups,
        'group': group,
    }
    return render(request, 'core/group.html', context)
