from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime

from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView

from core import models, forms

'''
def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'core/index.html', context)
'''


class AuthorizationForm(FormView):
    template_name = 'core/index.html'
    form_class = forms.AuthorizationForm
    success_url = '/teachers/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def form_valid(self, form):
        login, password = form.cleaned_data.values()
        teacher = models.Teacher.objects.get(login=login, password=password)
        id = teacher.pk
        form.redirection(f'/teachers/{id}')
        return super().form_valid(form)

'''
def get_all_schools(request):
    schools = models.School.objects.all()
    context = {
        'schools': schools,
        'title': 'Список классов'
    }
    return render(request, 'core/schools.html', context)

'''


class RedirectAdmin(RedirectView):
    query_string = True
    url = '/admin/'


class RedirectAuthorization(RedirectView):
    query_string = True
    url = '/accounts/login/'


class SchoolList(ListView):
    model = models.School
    context_object_name = "schools"
    template_name = 'core/schools.html'


class ScheduleList(ListView):
    model = models.Teacher
    template_name = 'core/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teacher = models.Teacher.objects.get(pk=self.kwargs['pk'])
        schedules = models.Schedule.objects.filter(teacher=teacher.pk)
        groups = models.Group.objects.filter(teacher=teacher.pk)

        context['teacher'] = teacher
        context['schedules'] = schedules
        context['groups'] = groups

        return context

'''
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
'''


class TeacherList(ListView):
    model = models.Teacher
    context_object_name = "teachers"
    template_name = 'core/teachers.html'


class GroupList(ListView):
    model = models.Group
    context_object_name = "groups"
    template_name = 'core/groups.html'


class LessonDetail(DetailView):
    model = models.Schedule
    template_name = 'core/lessons.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lesson = models.Lesson.objects.get(pk=self.kwargs['pk'])
        schedule = models.Schedule.objects.get(lesson=lesson.pk)
        teacher = models.Teacher.objects.get(pk=schedule.teacher.pk)
        groups = models.Group.objects.filter(teacher=teacher.pk)

        context['lesson'] = lesson
        context['groups'] = groups
        context['teacher'] = teacher
        return context


class HomeworkList(ListView):
    model = models.Lesson
    template_name = 'core/homeworks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lesson = models.Lesson.objects.get(pk=self.kwargs['pk'])
        schedule = models.Schedule.objects.get(lesson=lesson.pk)
        teacher = models.Teacher.objects.get(pk=schedule.teacher.pk)
        groups = models.Group.objects.filter(teacher=teacher.pk)
        homeworks = models.Homework.objects.filter(lesson=lesson.pk)

        context['lesson'] = lesson
        context['homeworks'] = homeworks
        context['groups'] = groups
        context['teacher'] = teacher
        return context

'''
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
'''


class GroupDetail(DetailView):
    model = models.Group
    template_name = 'core/group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teacher = models.Teacher.objects.get(group=self.kwargs['pk'])
        students = models.Student.objects.filter(group=self.kwargs['pk'])
        groups = models.Group.objects.filter(teacher=teacher.pk)

        context['students'] = students
        context['groups'] = groups
        context['teacher'] = teacher
        return context


class TeacherDetail(DetailView):
    model = models.Teacher
    template_name = 'core/teacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teacher = models.Teacher.objects.get(pk=self.kwargs['pk'])
        groups = models.Group.objects.filter(teacher=self.kwargs['pk'])

        context['teacher'] = teacher
        context['groups'] = groups
        return context


class SchoolDetail(DetailView):
    model = models.School
    template_name = 'core/school.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teacher = models.Teacher.objects.get(school=self.kwargs['pk'])
        groups = models.Group.objects.filter(teacher=teacher.pk)

        context['teacher'] = teacher
        context['groups'] = groups
        return context

