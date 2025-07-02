from django.shortcuts import render

# Create your views here.
""" As the name suggests, this is the index app view, the landing page """

def index(request):
    return render(request,"index/index.html")
