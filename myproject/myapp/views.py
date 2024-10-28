from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import cake_order_form


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

def cake_order_enter(request):
	
	if request.method=="POST":
		form=cake_order_form(request.POST)
		if form.is_valid():#Updates the form when a new value is added
			form.save()
	context={"form":cake_order_form()}
	return render(request,"cake_order_html.html",context)

def cake_order_details(request):
    if request.method == "POST": 
        f_name=request.POST['f_name'] 
        order_date=request.POST['order_date'] 
        cake_flavour=request.POST['cake_flavour']
    return HttpResponse(f'''<h3>Order Details</h3><br>Name:{f_name}<br>
                        Order Date:{order_date}<br>
                        Cake Flavour:{cake_flavour}''') 
    
