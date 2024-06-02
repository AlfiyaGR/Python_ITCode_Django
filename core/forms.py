from django import forms
from core import models


class PostTeacher(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ('surname', 'name', 'lastname', 'phone', 'email', 'login', 'password', 'subject')


class PostSchool(forms.ModelForm):
    class Meta:
        model = models.School
        fields = ('name', 'address', 'contactPhone')


class PostSubject(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = ('name',)


class PostAdmin(forms.ModelForm):
    class Meta:
        model = models.Administrator
        fields = ('surname', 'name', 'lastname', 'phone', 'email', 'login', 'password', 'school')

"""
class PostLesson(forms.Form):

    class Meta:
        model = models.Lesson
        fields = ('name', 'date', 'description', 'file', 'subject')


class PostSchedule(forms.ModelForm):
    class Meta:
        model = models.Schedule
        fields = ('group',)
"""