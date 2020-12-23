from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form, UserForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
def doctor_list(request):
    doctors = User.objects.all()
    return render(request, 'user/doctor_list.html', {'doctors':doctors})


def doctor_detail(request, slug):
    doctor_detail = Profile.objects.get(slug= slug)
    return render(request, 'user/doctor_detail.html', {'doctor_detail':doctor_detail})

def user_signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate( username=username, password=password)
            login(request, user)
            return redirect('accounts:doctor_list')
    else:
        form = UserForm()
    return render(request, 'user/user_signup.html', {'form':form})



def user_login(request):
    if request.method== "POST":
        form = Login_Form()
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:doctor_list')
    else:
        form = Login_Form
    return render(request, 'user/user_login.html', {'form':form})

@login_required()
def user_profile(request):
    
    return render(request, 'user/user_profile.html', {})


def update_profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('accounts:user_profile')
    return render(request, 'user/update_profile.html', {'user_form':user_form , 'profile_form': profile_form})


