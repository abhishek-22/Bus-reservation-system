from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm,PasswordResetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import SignupForm,ProfileupdateForm
from django.db.models import Q
from bus.models import BusDet,Bookingdets
from django.http import HttpResponse

def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username} successfully!')
            return redirect('Login')
    else:
        form = SignupForm()
    return render(request,'Signup.html', {'form': form})


@login_required
def view_profile(request):
    return render(request, 'viewprofile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileupdateForm( request.POST, instance=request.user )
        if form.is_valid():
            form.save()
            messages.success(request,"Your profile has been updated successfully")
            return redirect('view_profile')
        
    else:
        form = ProfileupdateForm(instance=request.user)
        return render(request, 'editprofile.html' , { 'form' : form })
    

def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, "Your password has been changed successfully")
            return redirect('view_profile')
        
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form': form})

   

