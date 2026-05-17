from django.db import models

# This creates a "Student" table in the database
class Student(models.Model):
    name = models.CharField(max_length=100)  # text column
    age  = models.IntegerField()              # number column

    def __str__(self):
        return self.name   # shows name when printed