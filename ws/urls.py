from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("send/", views.send),
    path("recover/", views.recover),
    path("get-token/", views.GET_TOKEN),
]