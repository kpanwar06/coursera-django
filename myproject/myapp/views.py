from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import cake_order_form


def home(request):
    return HttpResponse(f'''<h1><i><b><p style="background-color:aliceblue;color:rgb(28, 79, 110)">
                        Welcome to Sweet Shop!!</p></b></i></h1>''')

def inside_info(request):
    path=request.path
    scheme=request.scheme
    method=request.method
    path_info=request.path_info
    response=HttpResponse()
    response.headers['Age:']=20
    msg=f'''<h1><p style="background-color:aliceblue;color:rgb(28, 79, 110)" >Path Info</p></h1>
<br><h2>Path:{path}
<br>Scheme:{scheme}
<br>Method:{method}
<br>Path Info:{path_info}
<br>Responde Headers:{response.headers}</h2>
'''
    return HttpResponse(msg)

def cake_order_enter(request):
	
	if request.method=="POST":
		form=cake_order_form(request.POST)
		if form.is_valid():#Updates the form when a new value is added
			form.save()
	context={"form":cake_order_form()}
	return render(request,"cake_order_html.html",context)

def cake_order_details(request):
    flavours={1:"Chocolate",2:"Strawberry",3:"Vanilla"}
    if request.method == "POST": 
        f_name=request.POST['f_name'] 
        order_date=request.POST['order_date'] 
        cake_flavour=request.POST['cake_flavour']
    return HttpResponse(f'''<h3><p style="background-color:aliceblue;color:rgb(28, 79, 110)" >
                        Order Details</p>
                        </h3>
                        <br>Name:{f_name}<br>
                        Order Date:{order_date}<br>
                        Cake Flavour:{flavours[int(cake_flavour)]}''') 
    
