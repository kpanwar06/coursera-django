from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect 
from django.urls import reverse 

def home(request):
    return HttpResponse(f'<h1><b><i>Welcome to Sweet Treats!!!</i></b></h1>')

def inside_info(request):
    path=request.path
    scheme=request.scheme
    method=request.method
    path_info=request.path_info
    response=HttpResponse()
    response.headers['Age:']=20
    msg=f'''
<br>Path:{path}
<br>Scheme:{scheme}
<br>Method:{method}
<br>Path Info:{path_info}
<br>Responde Headers:{response.headers}
'''
    return HttpResponse(msg,content_type='text/html',charset='utf-8')

def flavours(request):
      return HttpResponse(f'''<h1>Flavours</h1>
                          <h2><ul>
                          <li>Chocolate</li><br>
                          <li>Strawberry</li><br>
                          <li>Coffee</li>
                          <ul></h2>''')

def order(request):
    return render(request,'form_order.html') 

def order_details(request): 
    if request.method == "POST": 
        name=request.POST['name'] 
        order_id=request.POST['order_id']
        t_dessert=request.POST['t_dessert'] 
        t_flavour=request.POST['t_flavour']
    return HttpResponse(f'''Name of Customer:{name}<br>Order Id:{order_id}<br>
                        Type of Dessert:{t_dessert}<br>Flavour:{t_flavour}''') 


    
