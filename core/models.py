from django.db import models


class School(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школа'

    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    surname = models.CharField('Фамилия', max_length=250)
    name = models.CharField('Имя', max_length=250)
    lastname = models.CharField('Отчество', max_length=250)
    phone = models.CharField('Номер телефона', max_length=50)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учитель'

    def __str__(self) -> str:
        return self.surname


class Student(models.Model):
    surname = models.CharField('Фамилия', max_length=250)
    name = models.CharField('Имя', max_length=250)
    lastname = models.CharField('Отчество', max_length=250)
    group = models.CharField('Класс', max_length=50)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученик'

    def __str__(self) -> str:
        return self.surname
