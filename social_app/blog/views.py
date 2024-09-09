from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def home(request):
    posts=Post.objects.all()
    if not posts.exists():
        posts=[{
            'title':'No Posts',
            'content':'No posts available',
            'date':'',
            'author':''
        }]

    

    return render(request,"home.html",{'posts':posts})

def about(request):
    return render(request,"about.html")
