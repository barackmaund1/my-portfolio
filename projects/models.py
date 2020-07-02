from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    photo = ImageField(manual_crop='1380x900')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def search_project(cls, technologies):
        return cls.objects.filter(title__icontains=technologies).all()    

class Person(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    subject=models.CharField(max_length=200,null=True,blank=True)
    message=models.TextField(max_length=250,null=True,blank=True)

    def __str__(self):
        return f'{self.name}'