# Generated by Django 5.0.4 on 2024-04-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=250, verbose_name='Отчество')),
                ('group', models.CharField(max_length=50, verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученик',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=250, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учитель',
            },
        ),
    ]
