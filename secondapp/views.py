from django.http import HttpResponse 

# Create your views here.

def greeting(request):

    return HttpResponse("<strong>Bonjour à tous de Secondapp!</strong>")

def message(request):

    return HttpResponse("<strong> This is the view.py of secondapp.</srrong>")    
