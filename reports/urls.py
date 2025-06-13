from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
        path('',views.ReportList.as_view(),name = 'index'),
        path('<pk>/detail/',views.ReportDetail.as_view(),name = 'detail'),
        path('save/',views.add_report,name='add_report'),
        ]
