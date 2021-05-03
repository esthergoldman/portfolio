from django.db import models
from datetime import datetime


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.first_name


class Project(models.Model):
    name = models.CharField(max_length=50)
    github =  models.URLField(blank=True)
    link =  models.URLField(blank=True)
    description = models.TextField(blank=True)
    tools = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name