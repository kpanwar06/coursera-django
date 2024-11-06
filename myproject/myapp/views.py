from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import cake_order_form


def home(request):
    return render(request,"home.html")

def inside_info(request):
    context={"path":request.path,"scheme":request.scheme,"method":request.method,
             "response":HttpResponse()}
    return render(request,"inside_info.html",context)

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
    
