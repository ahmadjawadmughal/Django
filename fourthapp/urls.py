from django.urls import path
#from . import views
from .views import intro,message

urlpatterns = [

    path("intro/", intro, name="intro"),
    path("message/", message, name="message"),
]


# thoughts urls.py


# users urls.py
