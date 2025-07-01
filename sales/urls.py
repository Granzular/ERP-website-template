from django.urls import path
from . import views
app_name = 'sales'

urlpatterns = [
        path('',views.home_view,name='home'),
        path('dashboard/',views.SalesDashboard.as_view(),name='dashboard'),
        path('sales/<pk>',views.SaleDetailView.as_view(),name='detail'),
        path('sales/upload_csv/',views.upload_csv,name="upload_csv"),

        ]
