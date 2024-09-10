from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignUpForm, UpdateProfileForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            # The cleaned_data attribute in Django forms is a dictionary-like object that holds validated form data after the form has been submitted and processed. This attribute is available after calling is_valid() on the form instance and is used to access the cleaned, validated data that has passed all validation checks defined in the form.
            messages.success(request,f'Account creation successful. Login to begin')
            return redirect('login')
        
    else:
        form=SignUpForm()

    return render(request,'signup.html',{'form':form})

@login_required
def profile(request):
    return render(request,'profile.html')

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UpdateProfileForm, UpdateUserForm

@login_required
def update_profile(request):
    # Initializing forms with the current user data
    update_user_form = UpdateUserForm(instance=request.user)
    update_profile_form = UpdateProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        update_user_form = UpdateUserForm(request.POST, instance=request.user)
        update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            # Check for changes before saving
            if update_user_form.has_changed():
                update_user_form.save()
            if update_profile_form.has_changed():
                update_profile_form.save()
                
            messages.success(request, 'Update successful')
            return redirect('profile')

    

    return render(request, 'update_profile.html', {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form
    })
