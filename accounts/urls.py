from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('doctor/', views.doctor_list, name = 'doctor_list'),
    path('login/', views.user_login, name = 'login'),
    path('signup/', views.user_signup, name = 'user_signup'),
    path('profile/', views.user_profile, name = 'user_profile'),
    path('update_profile/', views.update_profile, name = 'update_profile'),
    path('<slug:slug>/', views.doctor_detail, name = 'doctor_detail'),
]
