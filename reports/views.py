from django.shortcuts import render
from .models import Report
from django.views.generic import DetailView, ListView
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
# Create your views here.

class ReportList(ListView):
    
    model = Report
    template_name = "reports/index.html"
    context_object_name = "reports"


class ReportDetail(DetailView):

    model = Report
    template_name = "reports/detail.html"
    context_object_name = "report"

def save_pdf(request):
    pass

def add_report(request):
    
    if request.headers.get("X-Requested-With")=="XMLHttpRequest":
        name = request.POST.get('name')
        remark = request.POST.get('remark')
        image = get_report_image(request.POST.get('image'))
        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name,remark=remark,image=image,author=author)

        return JsonResponse({'msg':'send'})

