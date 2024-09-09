from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            # The cleaned_data attribute in Django forms is a dictionary-like object that holds validated form data after the form has been submitted and processed. This attribute is available after calling is_valid() on the form instance and is used to access the cleaned, validated data that has passed all validation checks defined in the form.
            messages.success(request,f'Account creation successful. Welcome {username}')
            return redirect('blog-home')
        
    else:
        form=SignUpForm()

    return render(request,'signup.html',{'form':form})