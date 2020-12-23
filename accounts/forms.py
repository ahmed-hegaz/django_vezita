from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserForm(forms.ModelForm):
    username = forms.CharField(label= "اسم المستخدم")
    first_name = forms.CharField(label= "الاسم الاول")
    last_name = forms.CharField(label= "الاسم الاخير") 
    email = forms.EmailField(label= "الايميل") 
    password1 = forms.CharField(label= "كلمة المرور", widget = forms.PasswordInput(), min_length=8) 
    password2 = forms.CharField(label= "تاكيد كلمة المرور", widget = forms.PasswordInput(), min_length=8) 
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class Login_Form(forms.ModelForm):
    username = forms.CharField(label= "اسم المستخدم")
    password = forms.CharField(label= "كلمة المرور", widget = forms.PasswordInput()) 
    class Meta:
        model = User
        fields = ("username", "password")

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label= "الاسم الاول")
    last_name = forms.CharField(label= "الاسم الاخير") 
    email = forms.EmailField(label= "الايميل") 
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class UpdateProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields = ("name", "surname","sub_title", "address",
        "address_detail", "phone","working_hours", "waitting_time", "who_i","price", "image",
        "specialist_doctor", "doctor","facebook", "twitter","youtube",
        
        
        )