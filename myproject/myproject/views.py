from django.http import HttpResponse

def handler404(request,exception):
    return HttpResponse(f'<h1>404 Error:Page not found!</h1><br><br> <button onclick="redirectToPage(http://127.0.0.1:8000/info/)">Go to Homepage</button>')