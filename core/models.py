import datetime

from django.db import models


class School(models.Model):
    name = models.CharField('Название', max_length=100)
    address = models.CharField('Адрес', max_length=50, default='address')
    contactPhone = models.CharField('Контактный телефон', max_length=100, default='phone')

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школа'

    def __str__(self) -> str:
        return f'{self.name}'


class Administrator(models.Model):
    surname = models.CharField('Фамилия', max_length=250)
    name = models.CharField('Имя', max_length=250)
    lastname = models.CharField('Отчество', max_length=250, null=True)
    phone = models.CharField('Номер телефона', max_length=50, null=True)
    email = models.CharField('Электронная почта', max_length=50, default='email')
    login = models.CharField('Логин', max_length=150, default='login')
    password = models.CharField('Пароль', max_length=150, default='password')

    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администратор'

    def __str__(self) -> str:
        return f'Админ {self.name} {self.lastname}'


class Teacher(models.Model):
    surname = models.CharField('Фамилия', max_length=250)
    name = models.CharField('Имя', max_length=250)
    lastname = models.CharField('Отчество', max_length=250, null=True)
    phone = models.CharField('Номер телефона', max_length=50, null=True)
    email = models.CharField('Электронная почта', max_length=50, default='email')
    login = models.CharField('Логин', max_length=150, default='login')
    password = models.CharField('Пароль', max_length=150, default='password')

    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return "/teacher/%i" % self.pk

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учитель'

    def __str__(self) -> str:
        return f'{self.name} {self.lastname} {self.subject.name} {self.school.name}'


class Group(models.Model):
    name = models.CharField('Класс', max_length=10)

    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return "/group/%i" % self.pk

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    surname = models.CharField('Фамилия', max_length=250)
    name = models.CharField('Имя', max_length=250)
    lastname = models.CharField('Отчество', max_length=250, null=True)
    phone = models.CharField('Номер телефона', max_length=50, default='phone')
    email = models.CharField('Электронная почта', max_length=50, default='email')
    login = models.CharField('Логин', max_length=150, default='login')
    password = models.CharField('Пароль', max_length=150, default='password')

    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученик'

    def __str__(self) -> str:
        return f'Ученик {self.name} {self.surname} {self.group.name}'


class Subject(models.Model):
    name = models.CharField('Предмет', max_length=100)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмет'

    def __str__(self):
        return f'{self.name}'


class GroupSubject(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Предметы классов'
        verbose_name_plural = 'Предметы классов'

    def __str__(self):
        return f'{self.subject.name} {self.group.name}'


class Lesson(models.Model):
    name = models.CharField('Урок', max_length=100, default='Урок')
    date = models.DateTimeField('Время')
    description = models.TextField('Описание', blank=True)
    file = models.FileField('Файл', null=True, upload_to='files', default=None)

    # schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Урок'

    def __str__(self) -> str:
        return f'{self.name} {self.subject} {self.date}'


class Schedule(models.Model):
    name = models.CharField('Расписание', max_length=100, default='Расписание')
    date = models.DateTimeField('Дата')

    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self) -> str:
        return f'{self.name} {self.group.name} {self.lesson.name}'


class Mark(models.Model):
    MARK_CHOICES = (
        ('выдано', 'выдано'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    mark = models.CharField('Оценка', max_length=50, choices=MARK_CHOICES, default='nothing')

    student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценка'

    def __str__(self):
        return f'{self.mark} {self.student}'


class Homework(models.Model):
    description = models.TextField('Описание', blank=True)
    date = models.DateTimeField('Дата выдачи')
    file = models.FileField('Файл', blank=True, null=True, upload_to='files', default=None)

    mark = models.ForeignKey('Mark', on_delete=models.CASCADE, null=True, default='выдано')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, default=None)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашнее задание'

    def __str__(self):
        return f'Домашнее задание {self.description}'
