from django.urls import path,re_path
from . import views

app_name='myapp'
urlpatterns = [
    # Add more URL patterns here
    path('path_para/<int:id>',views.path_para),
    path('qry_para/',views.qry_para),
    path('info/',views.info),
    path('showform/',views.showform),
    path('getform/',views.getform),
    path('new_view/',views.new_view),

]