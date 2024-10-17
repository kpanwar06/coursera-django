from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect 
from django.urls import reverse 

def info(request):
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

def path_para(request,id):
    name={1:"a",2:"b",3:"c"}
    x=name[id]
    return HttpResponse(f"<h1>id is:{id},name is:{x}</h1>")

def qry_para(request):
    name=request.GET['name']
    id=request.GET['id']
    return HttpResponse("Name:{},Id:{}".format(name,id))

def showform(request):
    return render(request,'form.html') 

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{},Id:{}".format(name, id)) 

def new_view(request):
    return HttpResponsePermanentRedirect(reverse('myapp/showform'))
