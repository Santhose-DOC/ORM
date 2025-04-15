from django.db import models
from django.contrib import admin
class Movie(models.Model):
    mid=models.IntegerField()
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    seat=models.CharField(max_length=20)
    email=models.EmailField()
    
class MovieAdmin(admin.ModelAdmin):
    list_display=('mid','name','type','seat','email')