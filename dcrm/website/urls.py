from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name=""),

    path('Home', views.home,name="Home"),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('logout', views.logout, name="logout"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),
]
