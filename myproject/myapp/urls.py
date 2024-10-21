from django.urls import path,re_path
from . import views

app_name='myapp'
urlpatterns = [
    # Add more URL patterns here
    path('inside_info/',views.inside_info),
    path('cake_order_view/',views.cake_order_view),
    path('',views.home),
]