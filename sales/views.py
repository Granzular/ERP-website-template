from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views import View
from .models import Sale, CSV
from .forms import SalesSearchForm
import pandas as pd
from .utils import get_customer_from_id, get_salesman_from_id,get_chart
from reports.forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def home_view(request):
    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()
    sales_df = None
    positions_df = None
    merged_df = None
    df = None
    chart = None
    no_data = None
    if request.method == "POST":
        try:
            org = request.user.staff.organization
        except:
            org = request.user.organization
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")
        result_by = request.POST.get("result_by")
        sale_qs = Sale.objects.filter(organization=org,created__date__gte=date_from,created__date__lte=date_to)
        if len(sale_qs) >0:
            sales_df = pd.DataFrame(sale_qs.values())
            sales_df["customer_id"] = sales_df["customer_id"].apply(get_customer_from_id)
            sales_df["salesman_id"] = sales_df["salesman_id"].apply(get_salesman_from_id)
            sales_df["created"] = sales_df["created"].apply(lambda x:x.strftime("%Y-%m-%d"))
            sales_df["updated"] = sales_df["updated"].apply(lambda x:x.strftime("%Y-%m-%d"))

            sales_df.rename({"customer_id":"customer","salesman_id":"salesman","id":"sales_id"},axis=1,inplace=True)
            
            positions_data = [] 

            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                            "position_id":pos.id,
                            "product":pos.product.name,
                            "quantity":pos.quantity,
                            "price":pos.price,
                            "sales_id":pos.get_sales_id(),
                            }
                    
                    positions_data.append(obj)
            positions_df = pd.DataFrame(positions_data)
            chart = get_chart(chart_type,result_by,sales_df)
            sales_df = sales_df.to_html()
             
        else:
            no_data = "No data available from the selected date range"


        context = {
               "searchform":search_form,
               "report_form":report_form,
               "sales_df":sales_df,
               "chart":chart,
               "no_data":no_data,
               }
        return render(request,'sales/home.html',context)
    context = {"searchform":search_form}

    return render(request,'sales/home.html',context)

class SalesDashboard(View):

    def get(self,request):
        return render(request,"sales/dashboard.html")

   
class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'

@login_required
def upload_csv(request):
    if request.headers.get("X-Requested-With")=="XMLHttpRequest":
        fd = request.FILES.get("file")
        if fd == None:
            raise ValueError
        CSV.objects.create(file_name=fd,organization=request.staff.organization)
        return JsonResponse({})
    return JsonResponse({})
