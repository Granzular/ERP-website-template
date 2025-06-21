from django.shortcuts import render

from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect,reverse
from .forms import LoginForm,SignupForm
from django.urls import resolve
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from .utils import get_org

def loginview(request):
    if request.method == "GET":
        form = LoginForm()
        context = {
                'login_form':form,
                }
        return render(request,"profiles/login.html",context)

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.clean()
            user = authenticate(username=cleaned_data.get('username'),password=cleaned_data.get('password'))
            if user is not None:
                login(request,user)
                next_url = request.GET.get("next")
                if next_url:
                    try:
                        resolve(urlparse(next_url).path)
                        return redirect(next_url)
                    except Resolver404:
                        return redirect(reverse("sales:index"))
                else:
                    return redirect(reverse("sales:index"))
            else:
                context = {
                        'error':'Invalid username or password',
                        'login_form':form,
                        }

                return render(request,'profiles/login.html',context)

        else:
            context = {
                    'error':'invalid form data',
                    'login_form':form,
                    }
            return render(request,'profiles/login.html',context)


def logoutview(request):
    try:
        logout(request)
    except:
        pass
    return redirect(reverse("profiles:login"))

def signupview(request):

    form = SignupForm(request.POST or None)

    if request.method == "GET":
        context = {
                'signup_form':form
                }
        return render(request,'profiles/signup.html',context)
    elif request.method == "POST":
        if form.is_valid():
            cld = form.clean()
            if cld.get('user_type')=='org':
                CustomUser.objects.create_user(username=cld.get('username'),email=cld.get('email'),password=cld.get('password'),user_type=cld_get('user_type'))
            elif cld.get('user_type')=='staff':
                instance = CustomUser.objects.create_user(username=cld.get('username'),email=cld.get('email'),password=cld.get('password'),user_type=cld_get('user_type'))
                Staff.objects.create(user=instance,organization=get_org(cld.get('public_key')))

            return redirect(reverse('profiles:login'))
        else:
            context = {
                    'signup_form':form,
                    'error':'invalid data',
                    }
            return render(request,'profiles/signup.html',context)

            
