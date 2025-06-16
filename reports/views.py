from django.shortcuts import render
from .models import Report
from django.views.generic import DetailView, ListView
from profiles.models import Profile
from django.http import JsonResponse,FileResponse
from .utils import get_report_image, get_report_pdf, cleanup


class ReportList(ListView):
    
    model = Report
    template_name = "reports/index.html"
    context_object_name = "reports"


class ReportDetail(DetailView):

    model = Report
    template_name = "reports/detail.html"
    context_object_name = "report"

def pdf(request,pk):
    fd, filename= get_report_pdf(pk)
    cleanup(filename)

    return FileResponse(fd,filename=filename)

def add_report(request):
    
    if request.headers.get("X-Requested-With")=="XMLHttpRequest":
        name = request.POST.get('name')
        remark = request.POST.get('remark')
        image = get_report_image(request.POST.get('image'))
        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name,remark=remark,image=image,author=author)

        return JsonResponse({'msg':'send'})

