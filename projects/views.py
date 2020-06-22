from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.views.generic import ListView
from .models import Post
# Create your views here.
class PostListView(ListView):
    model=Post
    template_name='projects/post_list.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']