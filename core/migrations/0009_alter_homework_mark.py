# Generated by Django 4.2.4 on 2024-05-07 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_homework_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='mark',
            field=models.ForeignKey(default='выдано', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.mark'),
        ),
    ]
