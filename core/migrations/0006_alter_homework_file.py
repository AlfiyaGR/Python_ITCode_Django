# Generated by Django 4.2.4 on 2024-05-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_homework_lesson_homework_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='file',
            field=models.FileField(null=True, upload_to='files', verbose_name='Файл'),
        ),
    ]
