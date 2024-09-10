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

@login_required
def update_profile(request):
    update_profile_form=UpdateProfileForm()
    update_user_form=UpdateUserForm()
    
    if request.method=='POST':

        update_user_form=UpdateUserForm(request.POST, instance=request.user)
        update_profile_form = UpdateProfileForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
    
        
        if update_profile_form.is_valid() and update_user_form.is_valid():
            update_user_form.save()
            update_profile_form.save()
            messages.success(request,f'Update successful')

            return redirect('profile')
    
        else:
            update_user_form = UpdateUserForm(instance=request.user)
            update_profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form
    }

    return render(request, 'update_profile.html', context)