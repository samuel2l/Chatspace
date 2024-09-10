from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile

class SignUpForm(UserCreationForm):
    #inheritting from user creation form so now it means any field we add here is something extra we need
    #in this cas we want the email field cos by default the form comes with only username and password
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']
class UpdateProfileForm(forms.ModelForm):
    #inheritting from user creation form so now it means any field we add here is something extra we need
    #in this cas we want the email field cos by default the form comes with only username and password
    class Meta:
        model=Profile
        fields=['dp']
