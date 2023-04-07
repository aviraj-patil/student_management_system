from django.db import models
import datetime
from django.db.models import Min

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    enrollment_number = models.CharField(max_length=10, unique=True, blank=False,default='',primary_key=True)
    roll_number = models.CharField(max_length=4, blank=True,default='')
    first_name = models.CharField(max_length=50, blank=False,default='')
    middle_name = models.CharField(max_length=50, blank=False,default='')
    last_name = models.CharField(max_length=50, blank=False,default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, default='M')
    email = models.EmailField(blank=False,default='')
    phone_number = models.CharField(max_length=10, blank=False,default='')
    date_of_birth = models.DateField(blank=False,default=datetime.date.today)
    address = models.TextField(blank=False,default='')
    is_approved = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE,primary_key=True)
    COURSE_CHOICES = (
        ('CO','Computer Engineering'),
        ('ME','Mechanical Engineering')
    )
    course_name = models.CharField(max_length=50, blank=False,choices= COURSE_CHOICES,default='CO')
    COURSE_YEAR =(
        ('1','First Sem'),
        ('2','Second Sem'),
        ('3','Third Sem'),
        ('4','Fourth Sem'),
        ('5','Fifth Sem'),
        ('6','Sixth Sem'),
    )
    course_sem = models.CharField(max_length=1,default='1',blank=False,choices=COURSE_YEAR)
    result_sem1 = models.CharField(max_length=2, default='')
    result_sem2 = models.CharField(max_length=2, default='')
    result_sem3 = models.CharField(max_length=2, default='')
    result_sem4 = models.CharField(max_length=2, default='')
    result_sem5 = models.CharField(max_length=2, default='')
    result_sem6 = models.CharField(max_length=2, default='')
    
    