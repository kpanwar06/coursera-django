from django.urls import path,re_path
from . import views

app_name='myapp'
urlpatterns = [
    # Add more URL patterns here
    path('inside_info/',views.inside_info),
    path('cake_order_enter/',views.cake_order_enter),
    path('cake_order_details/',views.cake_order_details),
    path('',views.home),
]