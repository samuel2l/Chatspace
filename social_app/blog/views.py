from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
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
#doing the home view as a class based view
class HomeView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='posts'#defines the name of the context you are sending to your template. by default it is called object
    ordering=['-date'] #field on which to order results. -date means date in descending order

class PostDetailsView(DetailView):
    model=Post
    template_name='post_details.html'
#if you do not specify a template name it means your template  should follow the convention: template/appname/model_viewtype.html



def about(request):
    return render(request,"about.html")
