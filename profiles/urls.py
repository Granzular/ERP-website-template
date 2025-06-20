from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
        path('accounts/login',views.loginview,name='login'),
        path('accounts/logout',views.logoutview,name='logout'),
        path('accounts/signup',views.signupview,name='signup'),
        ]
