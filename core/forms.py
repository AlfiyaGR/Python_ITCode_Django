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


class PostGroup(forms.ModelForm):
    class Meta:
        model = models.Group
        fields = ('name', 'teacher')


class PostStudent(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ('surname', 'name', 'lastname', 'phone', 'email', 'login', 'password', 'group')


class PostHomework(forms.ModelForm):
    class Meta:
        model = models.Homework
        fields = ('description', 'file')

