# Python_ITCode_Django

QuerySets:

In [3]: from core import models

In [4]: models.Teacher.objects.all()
Out[4]: <QuerySet [<Teacher: Алексей Петрович>, <Teacher: Петр Петрович>]>

In [5]: list(models.Homework.objects.all())
Out[5]: [<Homework: Домашнее задание 2024-05-07 14:35:19+00:00>]

In [7]: models.Group.objects.first()
Out[7]: <Group: 5Б>

In [8]: models.Group.objects.last()
Out[8]: <Group: 5Г>

In [9]: models.Group.objects.count()
Out[9]: 5

In [12]: models.Lesson.objects.order_by('date')
Out[12]: <QuerySet [<Lesson: Урок 2024-03-07 00:00:00+00:00>, <Lesson: Урок 2024-05-07 14:3
5:19+00:00>, <Lesson: Урок 2024-05-07 14:35:19+00:00>, <Lesson: Урок 2024-05-25 12:00:00+00
:00>, <Lesson: Урок 2024-05-31 06:00:00+00:00>]>

In [13]: models.Lesson.objects.order_by('-date')
Out[13]: <QuerySet [<Lesson: Урок 2024-05-31 06:00:00+00:00>, <Lesson: Урок 2024-05-25 12:0
0:00+00:00>, <Lesson: Урок 2024-05-07 14:35:19+00:00>, <Lesson: Урок 2024-05-07 14:35:19+00
:00>, <Lesson: Урок 2024-03-07 00:00:00+00:00>]>

In [16]: models.Group.objects.filter(name__contains='А')
Out[16]: <QuerySet [<Group: 5А>]>

In [17]: models.Group.objects.filter(name__contains='5')
Out[17]: <QuerySet [<Group: 5Б>, <Group: 5А>, <Group: 5В>, <Group: 5Г>]>

In [18]: models.Group.objects.filter(name__exact='5Г')
Out[18]: <QuerySet [<Group: 5Г>]>

In [20]: models.Homework.objects.filter(date__gt='2024-05-07')
Out[20]: <QuerySet [<Homework: Домашнее задание 2024-05-07 14:35:19+00:00>]>

In [24]: models.Homework.objects.filter(date__lt='2024-05-07')
Out[24]: <QuerySet [<Homework: Домашнее задание 2024-03-05 15:52:26+00:00>, <Homework: Домашнее задание 2024-04-19 00:00:00+00:00>]>

In [26]: models.Homework.objects.filter(date__lte='2024-05-07 14:35:19')
Out[26]: <QuerySet [<Homework: Домашнее задание 2024-05-07 14:35:19+00:00>, <Homework: Домашнее задание 2024-03-05 15:52:26+00:00>, <Homework: Домашнее задание 2024-04-19 00:00:00+00:00>]>

In [27]: models.Lesson.objects.latest('date')
Out[27]: <Lesson: Урок 2024-05-31 06:00:00+00:00>

In [28]: models.School.objects.get(id=1)
Out[28]: <School: Лицей>

In [29]: models.School.objects.filter(id=1).exists()
Out[29]: True

In [30]: models.School.objects.filter(id=3).exists()
Out[30]: False

In [31]: models.School.objects.create(name='Гимназия')
Out[31]: <School: Гимназия>

In [34]: models.School.objects.filter(id__gte=2).update(contactPhone='987766475')
Out[34]: 2

In [37]: models.School.objects.filter(id=3).delete()
Out[37]: (1, {'core.School': 1})

In [38]: models.School.objects.all()
Out[38]: <QuerySet [<School: Лицей>, <School: Школа>]>

In [39]: models.Schedule.objects.dates('date', 'day')
Out[39]: <QuerySet [datetime.date(2024, 5, 7)]>

In [41]: models.Lesson.objects.dates('date', 'day').reverse()
Out[41]: <QuerySet [datetime.date(2024, 5, 31), datetime.date(2024, 5, 25), datetime.date(2024, 5, 7), datetime.date(2024, 3, 7)]>

In [42]: models.School.objects.values('name', 'address')
Out[42]: <QuerySet [{'name': 'Лицей', 'address': 'Павлушево, 2'}, {'name': 'Школа', 'address': 'address'}]>

In [43]: models.School.objects.values_list('name', 'address')
Out[43]: <QuerySet [('Лицей', 'Павлушево, 2'), ('Школа', 'address')]>


