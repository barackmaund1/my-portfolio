from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.views.generic import ListView
from .models import Post,Person
from django.contrib import messages
from django.http import JsonResponse
from .email import send_welcome_email
# Create your views here.
class PostListView(ListView):
    model=Post
    template_name='projects/post_list.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('subject') and request.POST.get('email') and request.POST.get('message'):
            post=Person()
            post.name= request.POST.get('name')
            post.subject= request.POST.get('subject')
            post.email= request.POST.get('email')
            post.message= request.POST.get('message')
      
            post.save()
            messages.success(request, f'{post.name} Thank you.Your message has been received!') 
            return render(request, 'base.html')  

    else:
        return render(request,'base.html')

def home(request):
    return render(request, 'base.html')

def newsletter(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject=request.POST.get('subject')
    message=request.POST.get('message')
    
    recipient=Person(name=name,email=email,subject=subject,message=message)
    recipient.save()
    send_welcome_email(name,email)
    data = {'success': 'Your message has been successfully received and message sent to your email'}
    return JsonResponse(data)