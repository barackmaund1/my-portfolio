from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Post
# Create your views here.
class PostListView(ListView):
    model=Post
    template_name='index.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']