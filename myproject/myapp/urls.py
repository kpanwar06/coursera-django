from django.urls import path,re_path
from . import views

app_name='myapp'
urlpatterns = [
    # Add more URL patterns here
    path('flavours/',views.flavours),
    path('inside_info/',views.inside_info),
    path('order_details/',views.order_details),
    path('order/',views.order),
    path('',views.home),
]