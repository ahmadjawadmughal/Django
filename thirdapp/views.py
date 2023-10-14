from django.http import HttpResponse

# Create your views here.

def moment(request):

    return HttpResponse("<strong>J'utilise Django!<strong>")

def message(request):

    return HttpResponse("<strong>This is the thirdapp view.py</strong>")    
