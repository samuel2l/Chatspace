
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView
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

class CreatePostView(CreateView):
    model=Post
    fields=['title','content']
    template_name='create_post.html'
    #the post table takes the author id,title,content and date posted as args
    #date wil be filled automatically but how do we fill the author id in?
    #we will have to override the form_valid method, add the author id before continuing to check if valid
    #without this we will get error obv
    def form_valid(self,form):
        #so take the current form and set its author attribute as the current user
        form.instance.author=self.request.user
        #now proceed to do the normal checks the fucntion already does
        return super().form_valid(form)
#the create view expects its context to be called form


def about(request):
    return render(request,"about.html")
