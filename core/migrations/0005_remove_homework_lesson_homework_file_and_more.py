# Generated by Django 4.2.4 on 2024-05-07 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='lesson',
        ),
        migrations.AddField(
            model_name='homework',
            name='file',
            field=models.FileField(null=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.student'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=250, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='lastname',
            field=models.CharField(max_length=250, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name='Номер телефона'),
        ),
    ]