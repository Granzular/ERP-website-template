from django.urls import path
from . import views
app_name = 'sales'

urlpatterns = [
path('',views.index,name='index'),
        path('sales/',views.home_view,name='home'),
        path('sales/',views.SaleListView.as_view(),name='list'),
        path('sales/<pk>',views.SaleDetailView.as_view(),name='detail'),

        ]
