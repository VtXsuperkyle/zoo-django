from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name=""),

    path('register', views.register, name="register"),
]
