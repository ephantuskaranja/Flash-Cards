from django.db import models
from django.contrib.auth.models import User
import datetime as dt


# Create your models here.
class Course(models.Model):
    COURSE= (
        ('English', 'english'),
        ('Mathematics', 'mathematics'),
        ('Kiswahili', 'kiswahili'),
        ('Social Studies', 'social studies'),
        ('C.R.E', 'c.r.e'),
        ('I.R.E', 'i.r.e'),
        ('Science', 'science'),
    )
    name = models.CharField(max_length=30,choices=COURSE)
