from django.shortcuts import render, redirect
#from .forms import SignupForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from property.models import PropertyBook
from .forms import UserForm , ProfileForm , UserCreateForm





def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})



def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'profile/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST , request.FILES , instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:profile'))
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)       

    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form , 
        'profile_form' : profile_form
    })



def my_reservation(request):
    user_reservation = PropertyBook.objects.filter(name=request.user)
    return render(request,'profile/my_reservation.html' , {'user_reservation':user_reservation})