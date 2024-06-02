from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import datetime
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView
from core import models
from .forms import *

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


# Форма авторизации ученика
def get_admin(request):
    login = request.GET['login']
    password = request.GET['password']

    admin = models.Administrator.objects.get(login=login, password=password)

    return render(request, 'core/admin_panel.html', {'admin': admin, })


# Главная страница (вход учителя)
def home(request):
    return render(request, 'core/index.html')


# Главная страница (вход ученика)
def home_stud(request):
    return render(request, 'core/index_stud.html')


# Главная страница (вход администратора)
def home_admin(request):
    return render(request, 'core/index_admin.html')


""" Личный кабинет учителя """


def post_lesson(request, pk):
    teacher = models.Teacher.objects.get(pk=pk)
    subjects = models.Subject.objects.all()
    groups_schedule = models.Group.objects.all()
    groups = models.Group.objects.filter(teacher=teacher.pk)
    schedules = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    if request.method == "POST":
        lesson = models.Lesson()
        lesson.name = request.POST.get('name')
        lesson.date = request.POST.get('date')
        lesson.description = request.POST.get('description')
        lesson.file = request.POST.get('file')
        lesson.subject = models.Subject.objects.get(pk=request.POST.get('subject'))
        lesson.save()

        schedule = models.Schedule()
        schedule.name = request.POST.get('schedule')
        schedule.date = request.POST.get('date')
        schedule.teacher = teacher
        schedule.group = models.Group.objects.get(pk=request.POST.get('group'))
        schedule.lesson = lesson
        schedule.save()
        return redirect('schedule', pk=teacher.pk)

    return render(request, 'core/post_lesson.html',
                  {'subjects': subjects, 'schedules': schedules, 'groups': groups, 'groups_schedule': groups_schedule,
                   'teacher': teacher})


def edit_mark(request, pk, pk_hw):
    try:
        teacher = models.Teacher.objects.get(pk=pk)
        groups = models.Group.objects.filter(teacher=teacher.pk)
        homework = models.Homework.objects.get(pk=pk_hw)

        subject = models.Subject.objects.get(pk=homework.lesson.subject.pk)
        student = models.Student.objects.get(pk=homework.student.pk)
        marks = ['выдано', '1', '2', '3', '4', '5']

        if request.method == "POST":
            mark = models.Mark.objects.get(pk=homework.mark.pk)
            mark.mark = request.POST.get('mark')
            mark.student = student
            mark.subject = subject
            mark.save()

            homework.mark = mark
            homework.save()

            return redirect('homeworks', pk=homework.lesson.pk)

        return render(request, 'core/edit_mark.html',
                      {'teacher': teacher, 'groups': groups, 'marks': marks, 'homework': homework})

    except models.Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


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


class MarkDetail(DetailView):
    model = models.Student
    template_name = 'core/marks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = models.Student.objects.get(pk=self.kwargs['pk'])
        teacher = models.Teacher.objects.get(pk=student.group.teacher.pk)
        groups = models.Group.objects.filter(teacher=teacher.pk)
        marks = models.Mark.objects.filter(student=student.pk)

        context['marks'] = marks
        context['student'] = student
        context['teacher'] = teacher
        context['groups'] = groups
        return context


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


""" Личный кабинет ученика """


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


class StudMarkDetail(DetailView):
    model = models.Student
    template_name = 'core/marks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = models.Student.objects.get(pk=self.kwargs['pk'])
        # teacher = models.Teacher.objects.get(pk=student.group.teacher.pk)
        # groups = models.Group.objects.filter(teacher=teacher.pk)
        marks = models.Mark.objects.filter(student=student.pk)

        context['marks'] = marks
        context['student'] = student
        # context['teacher'] = teacher
        # context['groups'] = groups
        return context


# Подробности урока
class StudLessonDetail(DetailView):
    model = models.Lesson
    template_name = 'core/lessons.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = models.Student.objects.get(pk=self.kwargs['pk'])
        lesson = models.Lesson.objects.get(pk=self.kwargs['lesson_pk'])

        context['lesson'] = lesson
        context['student'] = student
        return context


# Список домашних работ по уроку
class StudHomeworkDetail(DetailView):
    model = models.Lesson
    template_name = 'core/homeworks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = models.Student.objects.get(pk=self.kwargs['pk'])
        lesson = models.Lesson.objects.get(pk=self.kwargs['lesson_pk'])
        homeworks = models.Homework.objects.filter(lesson=lesson.pk, student=student.pk)

        context['student'] = student
        context['lesson'] = lesson
        context['homeworks'] = homeworks
        return context


""" Личный кабинет администратора """


def edit_admin(request, pk):
    admin = get_object_or_404(models.Administrator, pk=pk)

    if request.method == "POST":
        form = PostAdmin(request.POST, instance=admin)

        if form.is_valid():
            admin = form.save(commit=False)
            admin.save()
            return redirect('administrator', pk=admin.pk)
    else:
        form = PostAdmin(instance=admin)
    return render(request, 'core/post_edit.html', {'form': form, 'admin': admin})


def edit_subject(request, pk, pk_subject):
    admin = models.Administrator.objects.get(pk=pk)
    subject = get_object_or_404(models.Subject, pk=pk_subject)

    if request.method == "POST":
        form = PostSubject(request.POST, instance=subject)

        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect('subjects', pk=admin.pk)
    else:
        form = PostSubject(instance=subject)
    return render(request, 'core/post_edit.html', {'form': form, 'admin': admin})


def post_subject(request, pk):
    admin = models.Administrator.objects.get(pk=pk)

    if request.method == "POST":
        form = PostSubject(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect('subjects', pk=admin.pk)
    else:
        form = PostSubject()
    return render(request, 'core/post_edit.html', {'form': form, 'admin': admin})


def delete_subject(request, pk, pk_subject):
    try:
        admin = models.Administrator.objects.get(pk=pk)
        subject = models.Subject.objects.get(pk=pk_subject)
        subject.delete()
        return redirect('subjects', pk=admin.pk)
    except models.Subject.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def post_teacher(request, pk):
    admin = models.Administrator.objects.get(pk=pk)

    if request.method == "POST":
        form = PostTeacher(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.school = admin.school
            teacher.save()
            return redirect('teachers', pk=admin.pk)
    else:
        form = PostTeacher()
    return render(request, 'core/post_edit.html', {'form': form, 'admin': admin})


def edit_teacher(request, pk, pk_teacher):
    admin = models.Administrator.objects.get(pk=pk)
    teacher = get_object_or_404(models.Teacher, pk=pk_teacher)

    if request.method == "POST":
        form = PostTeacher(request.POST, instance=teacher)

        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.school = admin.school
            teacher.save()
            return redirect('teachers', pk=admin.pk)
    else:
        form = PostTeacher(instance=teacher)
    return render(request, 'core/post_edit.html', {'form': form, 'admin': admin})


def delete_teacher(request, pk, pk_teacher):
    try:
        admin = models.Administrator.objects.get(pk=pk)
        teacher = models.Teacher.objects.get(pk=pk_teacher)
        teacher.delete()
        return redirect('teachers', pk=admin.pk)
    except models.Teacher.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def edit_school(request, pk, pk_school):
    admin = models.Administrator.objects.get(pk=pk)
    school = get_object_or_404(models.School, pk=pk_school)

    if request.method == "POST":
        form = PostSchool(request.POST, instance=school)

        if form.is_valid():
            school = form.save(commit=False)
            school.save()
            return redirect('admin_school', pk=admin.pk)
    else:
        form = PostSchool(instance=school)
    return render(request, 'core/post_edit.html', {'form': form, 'admin': admin})


def post_lesson_admin(request, pk):
    admin = models.Administrator.objects.get(pk=pk)
    subjects = models.Subject.objects.all()
    groups = models.Group.objects.all()
    teachers = models.Teacher.objects.all()
    schedules = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    if request.method == "POST":
        lesson = models.Lesson()
        lesson.name = request.POST.get('name')
        lesson.date = request.POST.get('date')
        lesson.description = request.POST.get('description')
        lesson.file = request.POST.get('file')
        lesson.subject = models.Subject.objects.get(pk=request.POST.get('subject'))
        lesson.save()

        schedule = models.Schedule()
        schedule.name = request.POST.get('schedule')
        schedule.date = request.POST.get('date')
        schedule.teacher = models.Teacher.objects.get(pk=request.POST.get('teacher'))
        schedule.group = models.Group.objects.get(pk=request.POST.get('group'))
        schedule.lesson = lesson
        schedule.save()
        return redirect('schedules', pk=admin.pk)

    return render(request, 'core/post_lesson.html',
                  {'subjects': subjects, 'schedules': schedules, 'groups_schedule': groups, 'teachers': teachers,
                   'admin': admin})


def edit_lesson_admin(request, pk, pk_lesson):
    try:
        admin = models.Administrator.objects.get(pk=pk)
        subjects = models.Subject.objects.all()
        groups = models.Group.objects.all()
        teachers = models.Teacher.objects.all()
        lesson = models.Lesson.objects.get(pk=pk_lesson)
        schedule = models.Schedule.objects.get(lesson=pk_lesson)
        schedules = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

        if request.method == "POST":
            lesson.name = request.POST.get('name')
            lesson.date = request.POST.get('date')
            lesson.description = request.POST.get('description')
            lesson.file = request.POST.get('file')
            lesson.subject = models.Subject.objects.get(pk=request.POST.get('subject'))
            lesson.save()

            schedule.name = request.POST.get('schedule')
            schedule.date = request.POST.get('date')
            schedule.teacher = models.Teacher.objects.get(pk=request.POST.get('teacher'))
            schedule.group = models.Group.objects.get(pk=request.POST.get('group'))
            schedule.lesson = lesson
            schedule.save()
            return redirect('schedules', pk=admin.pk)

        return render(request, 'core/edit_lesson.html',
                      {'subjects': subjects, 'schedules': schedules, 'groups_schedule': groups, 'teachers': teachers,
                       'admin': admin, 'lesson': lesson, 'schedule': schedule})

    except models.Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def delete_lesson(request, pk, pk_lesson):
    try:
        admin = models.Administrator.objects.get(pk=pk)
        lesson = models.Lesson.objects.get(pk=pk_lesson)
        lesson.delete()
        return redirect('schedules', pk=admin.pk)
    except models.Teacher.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


# Расписание учителя
class AllScheduleList(ListView):
    model = models.Administrator
    template_name = 'core/schedules.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        admin = models.Administrator.objects.get(pk=self.kwargs['pk'])
        schedules = models.Schedule.objects.all()

        context['admin'] = admin
        context['schedules'] = schedules

        return context


# Подробности о студенте
class AdminDetail(DetailView):
    model = models.Administrator
    template_name = 'core/admin_panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        admin = models.Administrator.objects.get(pk=self.kwargs['pk'])

        context['admin'] = admin
        return context


# Подробности о школе для ученика
class AdminSchoolDetail(DetailView):
    model = models.Administrator
    template_name = 'core/school.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        admin = models.Administrator.objects.get(pk=self.kwargs['pk'])
        school = models.School.objects.get(pk=admin.school.pk)

        context['school'] = school
        context['admin'] = admin
        return context


# Список всех учителей
class TeacherList(ListView):
    model = models.Administrator
    template_name = 'core/teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        admin = models.Administrator.objects.get(pk=self.kwargs['pk'])
        teachers = models.Teacher.objects.filter(school=admin.school.pk)

        context['admin'] = admin
        context['teachers'] = teachers
        return context


# Список всех классов
class GroupList(ListView):
    model = models.Administrator
    template_name = 'core/groups.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        admin = models.Administrator.objects.get(pk=self.kwargs['pk'])
        groups = models.Group.objects.filter(school=admin.school.pk)

        context['admin'] = admin
        context['groups'] = groups
        return context


# Список всех классов
class SubjectList(ListView):
    model = models.Administrator
    template_name = 'core/subjects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        admin = models.Administrator.objects.get(pk=self.kwargs['pk'])
        subjects = models.Subject.objects.all()

        context['admin'] = admin
        context['subjects'] = subjects
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
