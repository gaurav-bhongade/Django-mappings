# Generated by Django 3.2.20 on 2023-08-21 12:21

import college.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact', models.BigIntegerField()),
                ('elective_subject', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'STUDENT_MASTER',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('marks', models.FloatField()),
                ('teacher_name', models.CharField(max_length=50)),
                ('stud', models.ForeignKey(on_delete=models.SET(college.models.get_elective), to='college.student')),
            ],
            options={
                'db_table': 'SUBJECT_MASTER',
            },
        ),
    ]
