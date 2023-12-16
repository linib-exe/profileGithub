# core/models.py

from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.CharField(max_length =255, blank=True, null=True)
    github_link = models.CharField(max_length =255, blank=True, null=True)
    file_name = models.CharField(max_length=255, unique=True,null = True,blank  = True)  # New field for the filename

    def __str__(self):
        return self.full_name
