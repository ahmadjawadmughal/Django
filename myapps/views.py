from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def message(request):

    return HttpResponse("<strong>This is the Thirdapp of view.py</strong>")    
