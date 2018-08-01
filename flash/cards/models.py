from django.db import models
from django.contrib.auth.models import User



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

class Flshcard(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    notes = models.TextField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)