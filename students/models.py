from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    gpa = models.FloatField()
    registered_date = models.DateTimeField(auto_now_add=True)