from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.BigIntegerField()
    elective_subject = models.CharField(max_length=50)

    class Meta:
        db_table = 'STUDENT_MASTER'

def get_elective():
    return Student.objects.filter(name = 'Gaurav').first()

class Subject(models.Model):
    name = models.CharField(max_length=50)
    marks = models.FloatField()
    teacher_name = models.CharField(max_length=50)
    stud = models.ForeignKey(Student,on_delete=models.SET(get_elective))

    class Meta:
        db_table = 'SUBJECT_MASTER'
