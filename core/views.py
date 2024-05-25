from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView
from core import models, forms

""" Авторизация и главная страница """


# Форма авторизации учителя
def get_teacher(request):
    login = request.GET['login']
    password = request.GET['password']

    teacher = models.Teacher.objects.get(login=login, password=password)
    groups = models.Group.objects.filter(teacher=teacher.pk)

    return render(request, 'core/teacher.html', {'teacher': teacher, 'groups': groups})


# Форма авторизации ученика
def get_student(request):
    login = request.GET['login']
    password = request.GET['password']

    student = models.Student.objects.get(login=login, password=password)

    return render(request, 'core/student.html', {'student': student, })


# Главная страница (вход учителя)
def home(request):
    return render(request, 'core/index.html')


# Главная страница (вход ученика)
def home_stud(request):
    return render(request, 'core/index_stud.html')


""" Личный кабинет учителя """


# Расписание учителя
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


# Список студентов классов учителя
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


# Подробности об учителе
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


# Подробности о школе для учителя
class SchoolDetail(DetailView):
    model = models.Teacher
    template_name = 'core/school.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teacher = models.Teacher.objects.get(pk=self.kwargs['pk'])
        school = models.School.objects.get(pk=teacher.school.pk)
        groups = models.Group.objects.filter(teacher=teacher.pk)

        context['school'] = school
        context['teacher'] = teacher
        context['groups'] = groups
        return context


""" Личный кабинет ученика """


# Подробности о студенте
class StudentDetail(DetailView):
    model = models.Student
    template_name = 'core/student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = models.Student.objects.get(pk=self.kwargs['pk'])

        context['student'] = student
        return context


# Список учеников класса ученика
class StudGroupDetail(DetailView):
    model = models.Student
    template_name = 'core/stud_group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = models.Student.objects.get(pk=self.kwargs['pk'])
        group = models.Group.objects.get(pk=student.group.pk)
        teacher = models.Teacher.objects.get(group=group.pk)
        students = models.Student.objects.filter(group=group.pk)

        context['students'] = students
        context['student'] = student
        context['teacher'] = teacher
        return context


# Подробности о школе для ученика
class StudSchoolDetail(DetailView):
    model = models.Student
    template_name = 'core/school.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = models.Student.objects.get(pk=self.kwargs['pk'])
        school = models.School.objects.get(pk=student.group.school.pk)

        context['school'] = school
        context['student'] = student
        return context


""" Все остальное """


# Перенаправление на админскую панель
class RedirectAdmin(RedirectView):
    query_string = True
    url = '/admin/'


# Перенаправление на страницу автооризации (User)
class RedirectAuthorization(RedirectView):
    query_string = True
    url = '/accounts/login/'


# Список всех школ
class SchoolList(ListView):
    model = models.School
    context_object_name = "schools"
    template_name = 'core/schools.html'


# Расписание ученика
class StudScheduleList(ListView):
    model = models.Student
    template_name = 'core/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = models.Student.objects.get(pk=self.kwargs['pk'])
        group = models.Group.objects.get(pk=student.group.pk)
        schedules = models.Schedule.objects.filter(group=group.pk)

        context['student'] = student
        context['schedules'] = schedules
        context['group'] = group

        return context


# Список всех учителей
class TeacherList(ListView):
    model = models.Teacher
    context_object_name = "teachers"
    template_name = 'core/teachers.html'


# Список всех классов
class GroupList(ListView):
    model = models.Group
    context_object_name = "groups"
    template_name = 'core/groups.html'


# Подробности урока
class LessonDetail(DetailView):
    model = models.Lesson
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


# Список домашних работ по уроку
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
'''
