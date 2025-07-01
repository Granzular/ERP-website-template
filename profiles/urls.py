from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
        path('accounts/login/',views.loginview,name='login'),
        path('accounts/logout/',views.logoutview,name='logout'),
        path('accounts/signup/',views.signupview,name='signup'),
        path('accounts/profile/',views.home,name='home'),
        path('accounts/profile/change_profile_pic/',views.edit_profile_pic,name="edit_profile_pic"),
        ]
