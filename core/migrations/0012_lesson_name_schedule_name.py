# Generated by Django 4.2.4 on 2024-05-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_administrator'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='name',
            field=models.CharField(default='Урок', max_length=100, verbose_name='Урок'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='name',
            field=models.CharField(default='Расписание', max_length=100, verbose_name='Расписание'),
        ),
    ]
