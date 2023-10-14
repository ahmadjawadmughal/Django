from django.urls import path
from .views import greeting,message

urlpatterns = [

    path("greeting/", greeting, name="greeting"),
    path("message/", message, name="message"), 
]