from django.shortcuts import render
from .models import Report
from django.views.generic import DetailView, ListView
from profiles.models import Staff,Organization
from django.http import JsonResponse,FileResponse
from .utils import get_report_image, get_report_pdf, cleanup
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required,name="dispatch")
class ReportList(ListView):
    
    model = Report
    template_name = "reports/index.html"
    context_object_name = "reports"

    def get_queryset(self):
        qs = Report.objects.filter(organization = self.request.user.staff.organization)
        return qs

@method_decorator(login_required,name="dispatch")
class ReportDetail(DetailView):

    model = Report
    template_name = "reports/detail.html"
    context_object_name = "report"

@login_required
def pdf(request,pk):
    fd, filename= get_report_pdf(pk)
    cleanup(filename)

    return FileResponse(fd,filename=filename)

@login_required
def add_report(request):
    
    if request.headers.get("X-Requested-With")=="XMLHttpRequest":
        org = request.user.staff.organization
        name = request.POST.get('name')
        remark = request.POST.get('remark')
        image = get_report_image(request.POST.get('image'))
        author = Staff.objects.get(user=request.user)
        Report.objects.create(name=name,remark=remark,image=image,author=author,organization=org)
        print(name)

        return JsonResponse({'msg':'send'})
    else:
        print("OUTSIDE CONDITION")

