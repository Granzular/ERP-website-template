from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
from .utils import get_customer_from_id, get_salesman_from_id,get_chart
from reports.forms import ReportForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'sales/index.html')

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
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")
        result_by = request.POST.get("result_by")
        sale_qs = Sale.objects.filter(created__date__gte=date_from,created__date__lte=date_to)
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
            merged_df = pd.merge(sales_df,positions_df,on="sales_id")
            df = merged_df.groupby("transaction_id",as_index=False)['price'].agg('sum')

            chart = get_chart(chart_type,result_by,sales_df)
            positions_df = positions_df.to_html()
            sales_df = sales_df.to_html()
            merged_df = merged_df.to_html()
            df = df.to_html()
             
        else:
            no_data = "No data available from the selected date range"


        context = {
               "searchform":search_form,
               "report_form":report_form,
               "sales_df":sales_df,
               "positions_df":positions_df,
               "merged_df":merged_df,
               "df":df,
               "chart":chart,
               "no_data":no_data,
               }
        return render(request,'sales/home.html',context)
    context = {"searchform":search_form}

    return render(request,'sales/home.html',context)

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
   
class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'

