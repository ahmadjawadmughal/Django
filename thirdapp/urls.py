from django.urls import path
from .views import moment,message

urlpatterns = [

    path("moment/", moment, name = "moment"),
    path("message/", message, name="message"),
]