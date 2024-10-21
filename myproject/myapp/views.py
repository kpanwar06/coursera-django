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

def cake_order_view(request):
	form=cake_order_form()
	if request.method=="POST":
		form=cake_order_form(request.POST)
		if form.is_valid():#Updates the form when a new value is added
			form.save()
	context={"form":form}
	return render(request,"cake_order_html.html",context)
    
