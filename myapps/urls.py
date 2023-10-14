from django.urls import path

from . import views
#from .views import index

urlpatterns = [
    path("", views.index, name="index"),
    path("message/", views.message, name="message"),
]